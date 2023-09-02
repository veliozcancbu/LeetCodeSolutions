class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(remaining_nums, current_permutation):
            if not remaining_nums:
                result.append(current_permutation[:])
                return
            for i in range(len(remaining_nums)):
                current_permutation.append(remaining_nums[i])
                backtrack(remaining_nums[:i] + remaining_nums[i + 1:], current_permutation)
                current_permutation.pop()

        result = []
        backtrack(nums, [])
        return result

"""Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 
Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique."""