class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num_set = set(nums)

        i = 1
        while i in num_set:
            i += 1

        return i
#----------------------Another Solution-----------------------------
#--------------------Time Limit Exceeded----------------------------
"""class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        res = None

        nums = [x for x in nums if x > 0]

        if nums == []:
            return 1


        for j in range(1,max(nums)):
            if j not in nums:
                res = j
                break

        if res is None:
            res = max(nums)+1

        return res"""
#-------------------------------------------------------------------

"""Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1"""
