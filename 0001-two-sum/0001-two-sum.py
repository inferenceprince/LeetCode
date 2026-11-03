class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        hashmap = {}
        for i in range(0, len(nums)):

            compliment = target - nums[i]
            if compliment in hashmap:

                return [i, hashmap[compliment]]
            else:
                hashmap[nums[i]] = i