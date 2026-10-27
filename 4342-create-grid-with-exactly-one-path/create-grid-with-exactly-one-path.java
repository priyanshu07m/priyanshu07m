import java.util.*;

class Solution {
    public String[] createGrid(int m, int n) {
        List<String> result = new ArrayList<>();

        for (int i = 0; i < m; i++) {
            StringBuilder row = new StringBuilder();

            for (int j = 0; j < n; j++) {
                if (i == 0 || j == n - 1) {
                    row.append('.');
                } else {
                    row.append('#');
                }
            }

            result.add(row.toString());
        }

        return result.toArray(new String[0]);
    }
}