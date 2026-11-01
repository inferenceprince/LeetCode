class Solution:
    
    def removeElement(self, nums: list[int], val: int) -> int:
        
        n = len(nums)
        i: int = 0
        j: int = n - 1
        count: int = 0
        while i < j:

            if nums[i] == val:
                while(nums[j] == val and j > 0 and i != j):
                     j -= 1
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            i += 1

        for i in range(n - 1, -1, -1):
            if nums[i] == val:
                count += 1
        return n - count