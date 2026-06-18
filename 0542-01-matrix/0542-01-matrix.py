from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        vis = [[0 for _ in range(cols)] for _ in range(rows)]
        dis = [[0 for _ in range(cols)] for _ in range(rows)]

        queue = deque()
        # Add all 0s to the queue initially
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append(((r, c), 0))
                    vis[r][c] = 1

        # BFS traversal
        while queue:
            (i, j), d = queue.popleft()
            dis[i][j] = d
            for x, y in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                new_i, new_j = i + x, j + y   # FIXED: use i not j
                if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols:
                    continue
                if vis[new_i][new_j] == 1:
                    continue
                queue.append(((new_i, new_j), d + 1))
                vis[new_i][new_j] = 1

        return dis
