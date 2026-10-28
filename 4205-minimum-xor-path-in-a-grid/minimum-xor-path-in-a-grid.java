class Solution {
    public int minCost(int[][] grid) {
        int m = grid.length, n = grid[0].length;

        int mx = 0;
        for (int[] row : grid) {
            for (int x : row) {
                mx = Math.max(mx, x);
            }
        }

        // Next power of 2 greater than maximum grid value
        mx = 1 << (Integer.SIZE - Integer.numberOfLeadingZeros(mx));

        boolean[][][] f = new boolean[m][n][mx];

        f[0][0][grid[0][0]] = true;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {

                int x = grid[i][j];

                if (i == 0 && j == 0) continue;

                for (int k = 0; k < mx; k++) {

                    if (i > 0 && (k ^ x) < mx && f[i - 1][j][k ^ x]) {
                        f[i][j][k] = true;
                    }

                    if (j > 0 && (k ^ x) < mx && f[i][j - 1][k ^ x]) {
                        f[i][j][k] = true;
                    }
                }
            }
        }

        for (int k = 0; k < mx; k++) {
            if (f[m - 1][n - 1][k]) {
                return k;
            }
        }

        return -1;
    }
}