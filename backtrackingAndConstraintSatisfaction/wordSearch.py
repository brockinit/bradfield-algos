'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent"
cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Ex:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.


Assumptions:
  - Board and word can be None
  - Board will always be 2D
  - Word can contain more cells than spaces on the board
  -

:type board: List[List[str]]
:type word: str
:rtype: bool
'''
class Solution:

    def __init__(self):
        self.neighbors = [
            (0, -1),
            (0, 1),
            (1, 0),
            (-1, 0)
        ]

    def word_search(self, board, word):
        if board is None or word is None:
            return False

        cols = len(board[0])
        rows = len(board)

        # Word has more letters than spaces on the board
        if len(word) > cols * rows:
            return False

        # Create visited list for maintaining state
        visited = [[0 for x in range(cols)] for y in range(rows)]
        for r in range(rows):
            for c in range(cols):
                # Found first letter, set it in visited list
                if board[r][c] == word[0]:
                    visited[r][c] == 1
                # Base case. Word found in graph
                if self.next_letter_exists(board, r, c, visited, word[1:]):
                    return True
        # First letter never found in graph
        return False

    def next_letter_exists(self, board, r, c, visited, letters_left):
        # Base case. All letters in word have been found
        if len(letters_left) is 0:
            return True
        for n in self.neighbors:
            neighbor_row = r + n[0]
            neighbor_col = c + n[1]
            # Neighbor space being checked is within board boundaries
            if neighbor_row >= 0 and neighbor_col >= 0 and neighbor_row < len(board) and neighbor_col < len(board[0]):
                # Space has not been visited and letter matches next letter in the word
                if visited[neighbor_row][neighbor_col] is 0 and board[neighbor_row][neighbor_col] is letters_left[0]:
                    visited[neighbor_row][neighbor_col] = 1
                    # Recurse with the remaining letters. Will result in the base case of this function if true
                    if self.next_letter_exists(board, neighbor_row, neighbor_col, visited, letters_left[1:]):
                        return True
        return False





test_board = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
]

assert Solution().word_search(test_board, "ABCCED") == True, "ABCCED Should return True"
assert Solution().word_search(test_board, "SEE") == True, "SEE Should return True"
assert Solution().word_search(test_board, "ABCB") == False, "ABCB Should return False"