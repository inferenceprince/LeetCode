class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i: int = 0
        j: int = 0

        if n < 1:
            return None

        while i < m + j and j < n:
            
            if nums2[j] <= nums1[i]:

                nums1.insert(i, nums2[j])
                nums1.pop()
                j += 1
                
            i += 1

        while i < m + n and j < n: 
            nums1[i] = nums2[j]
            i += 1
            j += 1
            
