//https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/submissions/1196287294/
public class Solution {
    public string Tictactoe(int[][] moves) {
        List<int> row_res = Enumerable.Repeat(0,3).ToList();
        List<int> col_res = Enumerable.Repeat(0,3).ToList();
        int l_diag = 0;
        int r_diag = 0;
        int player = 1;

        List<(int, int)> l_diag_cells = new(){(0,0),(1,1),(2,2)};
        List<(int, int)> r_diag_cells = new(){(0,2),(1,1),(2,0)};
        foreach(var move in moves){
            (var r, var c) = (move[0], move[1]);
            row_res[r] += player;
            col_res[c] += player;

            if (l_diag_cells.Contains((r,c))){
                l_diag += player;
            }
            if (r_diag_cells.Contains((r,c))){
                r_diag += player;
            }
            if (Math.Abs(row_res[r]) == 3 || Math.Abs(col_res[c]) == 3 || Math.Abs(l_diag) == 3 || Math.Abs(r_diag) == 3) {
                return player == 1? "A" : "B";
            }

            player *=-1;
        }
        return moves.Length == 9? "Draw": "Pending";
    }
}