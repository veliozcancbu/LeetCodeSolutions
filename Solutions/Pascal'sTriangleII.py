class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        ans = [1]
        #ans = [0] * (rowIndex + 1)
        #ans[0] = ans[-1] = 1

        for i in range(1, rowIndex+1):
            # compute the i-th element of the current row
            num = (rowIndex-(i-1)) * ans[-1] // i
            ans.append(num) 
        return ans

"""Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
 

Constraints:

0 <= rowIndex <= 33
 

Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?"""