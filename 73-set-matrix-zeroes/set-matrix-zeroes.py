class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m, n = len(matrix), len(matrix[0])

        first_row_has_zero = False
        first_col_has_zero = False

        # Check first row
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_has_zero = True
                break

        # Check first column
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break

        # Use first row and column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set cells to zero based on markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Set first row to zero if needed
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Set first column to zero if needed
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0