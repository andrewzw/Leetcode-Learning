class Solution:
    def romanToInt(self, s: str) -> int:
        thislist = ["I", "V", "X", "L", "C", "D", "M"]
        thisdict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        total = 0
        s = (
            s.replace("IV", "IIII")
            .replace("IX", "VIIII")
            .replace("XL", "XXXX")
            .replace("XC", "LXXXX")
            .replace("CD", "CCCC")
            .replace("CM", "DCCCC")
        )
        for i in [*s]:
            for x in thislist:
                if i == x:
                    total += thisdict[x]

        return total


s = ["III", "LVIII", "MCMXCIV"]

for i in s:
    print(Solution().romanToInt(i))
