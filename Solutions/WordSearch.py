# 16. WordSearch.py
class Solution:
    def exist(self, board, word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c, idx):
            if idx == len(word): return True
            if r<0 or c<0 or r>=rows or c>=cols or board[r][c]!=word[idx]:
                return False
            temp, board[r][c] = board[r][c], "#"
            res = dfs(r+1,c,idx+1) or dfs(r-1,c,idx+1) or dfs(r,c+1,idx+1) or dfs(r,c-1,idx+1)
            board[r][c] = temp
            return res
        
        for i in range(rows):
            for j in range(cols):
                if dfs(i,j,0):
                    return True
        return False
