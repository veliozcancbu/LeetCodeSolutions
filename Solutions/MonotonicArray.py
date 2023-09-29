class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = decreasing = True

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                increasing = False
                break

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                decreasing = False
                break

        return increasing or decreasing

"""An array is monotonic if it is either monotone increasing or monotone decreasing.

An array is monotone increasing if for all , . An array is monotone decreasing if for all , .numsi <= jnums[i] <= nums[j]numsi <= jnums[i] >= nums[j]

Given an integer array , return if the given array is monotonic, or otherwise.numstruefalse

 

Example 1:

Input: nums = [1,2,2,3]
Output: true
Example 2:

Input: nums = [6,5,4,4]
Output: true
Example 3:

Input: nums = [1,3,2]
Output: false
 

Constraints:

1 <= nums.length <= 105
-105 <= nums[i] <= 105"""