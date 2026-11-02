class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < k:
            k = k % len(nums)
        nums[:] = nums[:-k][::-1] + nums[-k:][::-1]
        nums[:] = nums[::-1]
        
        