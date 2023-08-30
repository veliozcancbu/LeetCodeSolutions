class Solution(object):
    def letterCombinations(self, digits):

        if not digits:
            return []

        def getChars(digit):
            if digit == '2':
                return ['a', 'b', 'c']
            elif digit == '3':
                return ['d', 'e', 'f']
            elif digit == '4':
                return ['g', 'h', 'i']
            elif digit == '5':
                return ['j', 'k', 'l']
            elif digit == '6':
                return ['m', 'n', 'o']
            elif digit == '7':
                return ['p', 'q', 'r', 's']
            elif digit == '8':
                return ['t', 'u', 'v']
            elif digit == '9':
                return ['w', 'x', 'y', 'z']

        array = getChars(digits[0])

        if len(digits) == 1:
            return array

        for digit in digits[1:]:
            chars = getChars(digit)
            newArray = []
            for i in array:
                for j in chars:
                    newArray.append(i + j)
            array = newArray
        return array

'''Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].'''