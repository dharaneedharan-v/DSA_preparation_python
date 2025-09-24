def exist(board: list[list[str]], word: str) -> bool:
    m, n = len(board), len(board[0])
    L = len(word)
    def dfs(i,j,k):
        if k==L: return True
        if i<0 or j<0 or i>=m or j>=n or board[i][j]!=word[k]: return False
        tmp = board[i][j]; board[i][j]='#'
        res = (dfs(i+1,j,k+1) or dfs(i-1,j,k+1) or dfs(i,j+1,k+1) or dfs(i,j-1,k+1))
        board[i][j]=tmp
        return res
    for i in range(m):
        for j in range(n):
            if board[i][j]==word[0] and dfs(i,j,0):
                return True
    return False
