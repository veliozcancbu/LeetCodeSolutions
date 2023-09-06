class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        res = 0

        for i in zip(*strs):
            if list(i) != sorted(i):
                res += 1

        return res