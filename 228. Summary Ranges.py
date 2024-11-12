from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []  # array of ans
        i = 0  # start at 0

        while i < len(nums):  # i smaller than array size
            start = nums[i]  # start at first index

            # if not last and if nums at index i is == to next index value
            while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1  # move onto next

            # check if single num
            if start != nums[i]:
                ans.append(str(start) + "->" + str(nums[i]))
            else:
                ans.append(str(nums[i]))

            i += 1

        return ans


nums = [[0, 1, 2, 4, 5, 7], [0, 2, 3, 4, 6, 8, 9]]
for i in nums:
    print(Solution().summaryRanges(i))
