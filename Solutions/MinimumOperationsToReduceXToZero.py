from collections import defaultdict

class Solution:
    def minOperations(self, nums: 'List[int]', x: int) -> int:
        min_index = defaultdict(int)
        min_index[0] = 0
        prefix = 0

        for i, j in enumerate(nums, 1):
            prefix += j
            min_index[prefix] = i

        output = min_index[x] if x in min_index else float('inf')

        for i, j in enumerate(nums[::-1], 1):
            x -= j

            if x in min_index and min_index[x] + i <= len(nums):
                output = min(output, i + min_index[x])

        return output if output < float('inf') else -1

"""You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

 

Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
Example 2:

Input: nums = [5,6,7,8,9], x = 4
Output: -1
Example 3:

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 104
1 <= x <= 109"""