class Solution:
    
    def reverseVowels(self, s: str) -> str:
        i=0
        j=len(s)-1
        lis=list(s)
        while i<j:
            if  lis[i] not in "aeiouAEIOU":
                i=i+1
                continue
            if lis[j] not in "aeiouAEIOU":
                j=j-1
                continue
            lis[i],lis[j]=lis[j],lis[i]
            i=i+1
            j=j-1
        return "".join(lis)