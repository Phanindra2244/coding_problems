
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        l1=nums1[:m]
        l2=nums2[:n]
        l1.extend(l2)
        l1.sort()
        nums1[:]=l1