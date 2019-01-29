from collections import deque
import heapq


class Queue(object):
    """A basic FIFO queue"""

    def __init__(self):
        self._queue = deque()
    
    def add(self, x):
        self._queue.append(x)

    def pop(self):
        return self._queue.popleft()

    def empty(self):
        return len(self._queue) == 0


class Stack(object):
    """A FILO structure, just wrapping a Python list"""

    def __init__(self):
        self._stack = []

    def add(self, x):
        self._stack.append(x)

    def pop(self):
        return self._stack.pop()

    def empty(self):
        return len(self._stack) == 0


class PriorityQueue(object):
    """A structure that can be used either for UCS or A*"""

    def __init__(self):
        self._queue = []

    def add(self, x):
        heapq.heappush(self._queue, x)

    def pop(self):
        return heapq.heappop(self._queue)

    def empty(self):
        return len(self._queue) == 0

