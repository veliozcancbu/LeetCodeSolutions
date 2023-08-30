class Solution:
    def isPalindrome(self, x: int) -> bool:

        x_list = list(str(x))
        #new = []

        reversed_x = list(x_list[::-1])

        if x_list == reversed_x:
            return True
        return False

'''Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1'''



