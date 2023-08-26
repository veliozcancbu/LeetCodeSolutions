class Solution:
    def romanToInt(self, s: str) -> int:
        # Soldan sağa okunan arrayde roman[s[i]] roman[s[i+1]]'den küçükse-> i = -,
        # roman[s[i]] roman[s[i+1]]'den büyükse -> i = +
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sonuc = 0

        for i in range(len(s)):
            if i+1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                sonuc -= roman[s[i]]
            else:
                sonuc += roman[s[i]]

        return sonuc

