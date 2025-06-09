class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        current = 1
        position = 1

        while position < k:
            gap = self._calculate_gap(current, current + 1, n)
            if position + gap <= k:
                current += 1
                position += gap
            else:
                current *= 10
                position += 1

        return current

    def _calculate_gap(self, left: int, right: int, n: int) -> int:
        gap = 0
        while left <= n:
            gap += min(n + 1, right) - left
            left *= 10
            right *= 10
        return gap

"""
Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].

 

Example 1:

Input: n = 13, k = 2
Output: 10
Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
Example 2:

Input: n = 1, k = 1
Output: 1
 

Constraints:

1 <= k <= n <= 109
"""
