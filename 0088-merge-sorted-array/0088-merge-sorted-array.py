class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i: int = m - 1
        j: int = n - 1
        k: int = m + n - 1
        if n < 1:
            return None

        while j > -1 and i > -1:

            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1

        while j > -1:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1