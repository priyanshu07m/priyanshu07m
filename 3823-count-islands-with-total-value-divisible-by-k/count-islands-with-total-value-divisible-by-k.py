from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        res = 0

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 0:
                    continue

                island_sum = grid[r][c]
                grid[r][c] = 0
                stack = [(r, c)]

                while stack:
                    x, y = stack.pop()

                    for nx, ny in (
                        (x + 1, y),
                        (x - 1, y),
                        (x, y + 1),
                        (x, y - 1)
                    ):
                        if (
                            0 <= nx < n
                            and 0 <= ny < m
                            and grid[nx][ny] > 0
                        ):
                            island_sum += grid[nx][ny]
                            grid[nx][ny] = 0
                            stack.append((nx, ny))

                if island_sum % k == 0:
                    res += 1

        return res