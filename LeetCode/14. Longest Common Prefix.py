from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min = float("inf")

        # find min leng
        for word in strs:
            if len(word) < min:
                min = len(word)

        i = 0
        while i < min:
            for word in strs:
                if word[i] != strs[0][i]:
                    return word[:i]
            i += 1
        return word[:i]


strs = [["flower", "flow", "flight"], ["dog", "racecar", "car"]]
for i in strs:
    print(Solution().longestCommonPrefix(i))
