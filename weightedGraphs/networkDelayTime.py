import heapq
import collections

'''
  Assumptions:
    N will be in the range [1, 100].
    K will be in the range [1, N].
    The length of times will be in the range [1, 6000].
    All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 1 <= w <= 100.

    :type times: List[List[int]]
    :type N: int
    :type K: int
    :rtype: int
'''
def network_delay_time(times, N, K):
    graph = collections.defaultdict(list)
    for src, tgt, time in times:
        graph[src].append([tgt, time])
    distances = {}
    pq = [[0, K]]

    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_vertex in distances:
            continue
        distances[current_vertex] = current_distance
        for neighbor, neighbor_distance in graph[current_vertex]:
            if neighbor not in distances:
                heapq.heappush(pq, [neighbor_distance + current_distance, neighbor])

    # 1 or more nodes were unable to be reached from the given starting node
    if len(distances) != N:
        return -1

    # Return the furthest distance from the starting node to another node on the graph
    return max(distances.values())


assert network_delay_time([[2,1,1],[2,3,1],[3,4,1]], 4, 2) == 2, "Expected 2"
