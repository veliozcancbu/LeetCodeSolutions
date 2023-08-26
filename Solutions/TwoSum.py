class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Create a dictionary to hold index and value
        calculated = {}
        #target - n = sub, if sub in dict then return indexes, otherwise add index and value to dict
        for i, n in enumerate(nums):
            sub = target - n
            if sub in calculated:
                return [calculated[sub], i]
            calculated[n] = i
        return
