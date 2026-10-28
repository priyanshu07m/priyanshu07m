class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r: int, c: int):
            if (
                r < 0
                or c < 0
                or r >= ROWS
                or c >= COLS
                or grid[r][c] == 1
            ):
                return

            grid[r][c] = 1

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Remove islands connected to boundary
        for r in range(ROWS):
            for c in range(COLS):
                if (
                    (r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1)
                    and grid[r][c] == 0
                ):
                    dfs(r, c)

        closed_islands = 0

        # Count remaining islands
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    closed_islands += 1
                    dfs(r, c)

        return closed_islands