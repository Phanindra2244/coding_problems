class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        k=s.split()
        ans= (k[::-1])
        ans=ans[:len(ans)]
        return " ".join((ans))