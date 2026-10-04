class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        n=len(mat)
        s=0
        for i in range(n):
            s=s+mat[i][i]
            s=s+mat[i][n-1-i]
        if(n%2==1):
            s-=mat[n//2][n//2]
        return s