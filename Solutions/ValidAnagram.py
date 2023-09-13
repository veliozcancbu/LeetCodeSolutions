from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        dict_1 = defaultdict(int)
        dict_2 = defaultdict(int)

        for i in s:
            dict_1[i] += 1

        for j in t:
            dict_2[j] += 1

        if dict_1 == dict_2:
            return True
        else:
            return False

"""Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?"""