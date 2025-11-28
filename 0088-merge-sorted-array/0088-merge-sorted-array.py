class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        if m == 0:
            nums1[:] = nums2

        elif n != 0:


            while (len(nums1) - m) > 0:
                nums1.pop()
            while (len(nums2) - n) > 0:
                nums2.pop()
            
            nums1.extend(nums2)
            nums1[:] = sorted(nums1)
                     