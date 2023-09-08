class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows < 0:
            return []

        output = [[1]]

        for i in range(1, numRows):
            pascal = map(lambda x, y: x + y, output[-1] + [0], [0] + output[-1])
            output.append(list(pascal))

        return output
"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30
"""
