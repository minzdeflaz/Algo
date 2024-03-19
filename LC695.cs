//https://leetcode.com/problems/max-area-of-island/description/
public class Solution {
    public int MaxAreaOfIsland(int[][] grid) {
        HashSet<(int,int)> visited = new();
        LinkedList<(int,int)> to_visit = new();

        int ROWS = grid.Length;
        int COLS = grid[0].Length;

        int max_area = 0;
        int cur_area = 0;
        List<(int, int)> directions = new() {(0,-1),(0,1),(-1,0),(1,0)};
        for (int i =0; i<ROWS; i++){
            for (int j =0; j<COLS; j++){
                if (grid[i][j] == 1 && !visited.Contains((i,j))) {
                    to_visit.AddLast((i,j));
                    visited.Add((i, j));

                }

                while (to_visit.Count !=0 ){
                    (var cur_i, var cur_j) = to_visit.First();
                    to_visit.RemoveFirst();
                    cur_area+=1;

                    foreach ((var x, var y) in directions){
                        int i_n = cur_i+x;
                        int j_n = cur_j+y;

                        if (0<=i_n && i_n<ROWS && 0<=j_n && j_n<COLS && grid[i_n][j_n]==1 && !visited.Contains((i_n,j_n))) {
                            to_visit.AddLast((i_n, j_n));
                            visited.Add((i_n, j_n));
                        }
                    }
                }
                max_area = Math.Max(max_area, cur_area);
                cur_area = 0;
            }
        }
        return max_area;
        
    }
}