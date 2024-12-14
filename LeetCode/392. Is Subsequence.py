class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        S = len(s)
        T = len(t)

        if s == "":
            return True
        if S > T:
            return False

        j = 0
        for i in range(T):
            if t[i] == s[j]:
                if j == S - 1:  # last index(the end)
                    return True
                j += 1  # move to next

        return False


s = ["abc", "axc"]
t = ["ahbgdc", "ahbgdc"]
for i in range(len(s)):
    print(Solution().isSubsequence(s[i], t[i]))
