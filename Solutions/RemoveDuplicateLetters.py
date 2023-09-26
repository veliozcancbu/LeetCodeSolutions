from collections import defaultdict

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        dict = defaultdict(int)
        is_in = defaultdict(bool)

        ans = []

        for i in s:
            dict[i] += 1

        for j in s:
            dict[j] -= 1

            if is_in[j]:
                continue

            while ans and j < ans[-1] and dict[ans[-1]] > 0:
                is_in[ans.pop()] = False

            ans.append(j)
            is_in[j] = True

        return ''.join(str(x) for x in ans)

"""Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is 
the smallest in lexicographical order
 among all possible results.

 

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
 

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/"""

