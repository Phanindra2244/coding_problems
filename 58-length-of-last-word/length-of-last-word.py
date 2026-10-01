class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        k= s.strip()
        l=len(k)
        c=0
        for i in range(l-1,-1,-1):
            if(k[i]==" "):
                break
            c=c+1
        return c
