class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        
        i: int = 0
        j: int = 0  
        n: int = len(nums)

        while i < n and j < n:
            if nums[i] != nums[j]:

                nums[i + 1] = nums[j]
                i += 1
            j += 1


        return i + 1