class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = []
        len1, len2 = len(word1), len(word2)
        x = 0

        # Merge characters alternately until one of the words is fully processed
        while x < len1 or x < len2:
            if x < len1:
                merged.append(word1[x])
            if x < len2:
                merged.append(word2[x])
            x += 1

        # Join the list into a single string
        return "".join(merged)


word1 = ["abc", "ab", "abcd"]
word2 = ["pqr", "pqrs", "pq"]

for i in range(len(word1)):
    print(Solution().mergeAlternately(word1[i], word2[i]))
