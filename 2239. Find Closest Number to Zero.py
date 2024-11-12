class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        closer = nums[0]
        for x in nums:
            if abs(x) < abs(closer):
                closer = x
        if closer < 0 and abs(closer) in nums:
            return abs(closer)
        else:
            return closer

        return closer


nums = [[-4, -2, 1, 4, 8], [2, -1, 1]]

for i in nums:
    print(Solution().findClosestNumber(i))
