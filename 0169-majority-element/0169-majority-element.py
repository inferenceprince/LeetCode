class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        
        nums.sort()
        max_found = [0, 0]
        i, j = 0, 0
        current_found = [nums[i], 0]
        while j < len(nums):

            if nums[i] == nums[j]:
                current_found[1] += 1
            else:
                if current_found[1] > max_found[1]:
                    max_found = current_found
                i = j
                current_found = [nums[i], 1]
            j += 1
        
        
        if current_found[1] > max_found[1]:
            return current_found[0]
        return max_found[0]
                