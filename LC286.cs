//https://leetcode.com/problems/walls-and-gates/submissions/1203807625/
public class Solution {
    public void WallsAndGates(int[][] rooms) {
        int INF = 2147483647;
        int ROWS = rooms.Length;
        int COLS =rooms[0].Length;
        HashSet<(int, int)> visited = new();
        LinkedList<(int, int, int)> queue = new();
        for (int i = 0; i < ROWS; i++) {
            for (int j = 0; j <COLS; j++) {
                if (rooms[i][j] == 0){
                    queue.AddLast((i, j, 0));
                    visited.Add((i, j));
                }
                
            }
        }

        List<(int,int)> directions = new() {(-1, 0) , (1, 0), (0, -1), (0, 1)};

        while (queue.Count !=0) {
            (var i, var j, var dis) = queue.First.Value;
            rooms[i][j] = dis;
            queue.RemoveFirst();

            foreach ((var x, var y) in directions) {
                var i_n = i + x;
                var j_n = j + y;

                if (0 <= i_n && i_n<ROWS && 0 <= j_n && j_n<COLS && !visited.Contains((i_n, j_n)) && rooms[i_n][j_n] != -1) {
                    queue.AddLast((i_n, j_n, dis+1));
                    visited.Add((i_n, j_n));
                }
            }
        }
    }
}