class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            ch=needle
            return haystack.index(ch)
        else:
            return -1