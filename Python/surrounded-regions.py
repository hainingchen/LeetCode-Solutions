# Time:  O(m * n)
# Space: O(m + n)

import collections


class Solution(object):
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if not board:
            return
        q = collections.deque([])

        for i in xrange(len(board)):
            q.append((i, 0))
            q.append((i, len(board[0]) - 1))

        for j in xrange(len(board[0])):
            q.append((0, j))
            q.append((len(board) - 1, j))

        while q:
            i, j = q.popleft()
            if board[i][j] in ['O', 'V']:
                board[i][j] = 'V'
                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= x < len(board) and 0 <= y < len(board[0]) and \
                       board[x][y] == 'O':
                        board[x][y] = 'V'
                        q.append((x, y))

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] != 'V':
                    board[i][j] = 'X'
                else:
                    board[i][j] = 'O'

