from collections import defaultdict

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if not s:
            return True
        if not t:
            return False

        dict = defaultdict(int)
        counter = 0

        for i in s:
            dict[i] += 1

        for i in t:
            if dict[i] > 0:
                if s[counter] == i:
                    counter += 1
                    dict[i] -= 1

        return counter == len(s)

"""Given two strings and , return if is a subsequence of , or otherwise.sttruestfalse

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., is a subsequence of while is not)."ace""abcde""aec"

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and consist only of lowercase English letters.t
 

Follow up: Suppose there are lots of incoming , say where , and you want to check one by one to see if has its subsequence. 
In this scenario, how would you change your code?ss1, s2, ..., skk >= 109t"""