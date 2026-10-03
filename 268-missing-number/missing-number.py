class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        m=max(nums)
        s=min(nums)
        n=len(nums)
        total=(n*(n+1))/2
        for i in range(n+1):
            if((total-i)==sum(nums)):
                return i