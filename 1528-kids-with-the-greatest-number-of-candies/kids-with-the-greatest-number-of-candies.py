class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        lis=[]
        
        for i in candies:
            if i+extraCandies>=max(candies):
                lis.append(True)
            else:
                lis.append(False)
        return lis