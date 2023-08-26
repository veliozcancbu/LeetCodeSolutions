class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        for i in range(len(strs[0])):
            for j in strs:
                if i == len(j) or j[i] != strs[0][i]:
                    return lcp
            lcp += strs[0][i]

        return lcp