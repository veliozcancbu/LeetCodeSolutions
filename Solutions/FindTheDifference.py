class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        for i in t:
            if s.count(i) != t.count(i):
                return i

#---------------------Another Solution----------------------
#-----------------------------------------------------------
#class Solution:
#    def findTheDifference(self, s: str, t: str) -> str:
#
#        ans = 0
#
#        for i in t:
#            ans^= ord(i)
#
#        for j in s:
#            ans^= ord(j)
#
#        return chr(ans)
#-----------------------------------------------------------

"""You are given two strings s and t.

String t is generated by random shuffling string s and then add one more letter at a random position.

Return the letter that was added to t.

 

Example 1:

Input: s = "abcd", t = "abcde"
Output: "e"
Explanation: 'e' is the letter that was added.
Example 2:

Input: s = "", t = "y"
Output: "y"
 

Constraints:

0 <= s.length <= 1000
t.length == s.length + 1
s and t consist of lowercase English letters."""
