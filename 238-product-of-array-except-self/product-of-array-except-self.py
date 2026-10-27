class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans=[]
        if 0 not in nums:
         p=1
         for i in nums:
            p=p*i
         for i in nums:
            k=p//i
            ans.append(k)
        else:
            if nums.count(0)>1:
                return [0]*len(nums)
            p=1
            for j in nums:
                if j!=0:
                    p=p*j
            for i in nums:
                if i==0:
                    ans.append(p)
                else:
                    ans.append(0)
        return ans
        

        