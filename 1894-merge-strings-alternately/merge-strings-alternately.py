class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l=[]
        ls1=list(word1)
        ls2=list(word2)
        n1=len(ls1)
        n2=len(ls2)
        n=max(n1,n2)
        for i in range(n):
            if i<n1:
                l.append(ls1[i])
            if i<n2:
                l.append(ls2[i])
        res=("".join(l))
        return res
