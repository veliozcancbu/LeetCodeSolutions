class Solution:
    def minimumSum(self, num: int) -> int:
        a = str(num)
        num_digit = [a[0], a[1], a[2], a[3]]

        min_value = min(num_digit)
        num_digit.remove(min_value)

        min_value_2 = min(num_digit)
        num_digit.remove(min_value_2)

        new_1 = (int(min_value) * 10) + int(num_digit[0])
        new_2 = (int(min_value_2) * 10) + int(num_digit[1])

        return new_1 + new_2

       #-------------------------------Another Solution-------------------------------------------------------------
       
       #class Solution:
       #     def minimumSum(self, num: int) -> int:
       #         num_digit = sorted(list(str(num)))
       # 
       #         return (int(num_digit[0]) * 10) + int(num_digit[2]) + (int(num_digit[1]) * 10) + int(num_digit[3])
       
       #------------------------------------------------------------------------------------------------------------



'''You are given a positive integer num consisting of exactly four digits. Split num into two new integers new1 and new2 by using the digits found in num. Leading zeros are allowed in new1 and new2, and all the digits found in num must be used.

For example, given num = 2932, you have the following digits: two 2's, one 9 and one 3. Some of the possible pairs [new1, new2] are [22, 93], [23, 92], [223, 9] and [2, 329].
Return the minimum possible sum of new1 and new2.

 

Example 1:

Input: num = 2932
Output: 52
Explanation: Some possible pairs [new1, new2] are [29, 23], [223, 9], etc.
The minimum sum can be obtained by the pair [29, 23]: 29 + 23 = 52.
Example 2:

Input: num = 4009
Output: 13
Explanation: Some possible pairs [new1, new2] are [0, 49], [490, 0], etc. 
The minimum sum can be obtained by the pair [4, 9]: 4 + 9 = 13.
 

Constraints:

1000 <= num <= 9999'''
