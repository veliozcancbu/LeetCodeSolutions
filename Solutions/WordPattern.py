from collections import defaultdict

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        n = len(pattern)

        if n != len(s):
            return False

        dict_1 = defaultdict(str)
        dict_2 = defaultdict(str)

        for i in range(n):
            if s[i] in dict_1 and dict_1[s[i]] != pattern[i]:
                return False
            if pattern[i] in dict_2 and dict_2[pattern[i]] != s[i]:
                return False

            dict_1[s[i]] = pattern[i]
            dict_2[pattern[i]] = s[i]

        return True

"""Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
 

Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space."""