class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        d = defaultdict(list)
        n = len(s)

        for w in dictionary:
            d[w[0]].append(w)

        res = (n + 1) * [0]

        for i in range(n - 1, -1, -1):
            res[i] = res[i + 1] + 1

            if s[i] in d:
                for w in d[s[i]]:
                    if s[i:i + len(w)] == w:
                        res[i] = min(res[i], res[i + len(w)])

        return res[0]

""" class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        d = defaultdict(list)
        n = len(s)

        for w in dictionary:
            d[w[0]].append(w)

        res = (n + 1) * [0]

        for i in range(n - 1, -1, -1):
            res[i] = res[i + 1] + 1

            if s[i] in d:
                for w in d[s[i]]:
                    if s[i:i + len(w)] == w:
                        res[i] = min(res[i], res[i + len(w)])

        return res[0] """
