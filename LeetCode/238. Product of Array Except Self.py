from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        answer = [1] * len(nums)
        prefix = 1
        postfix = 1

        # Calculate prefix products
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]

        # Calculate postfix products and combine
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]
        return answer


nums = [[1, 2, 3, 4], [-1, 1, 0, -3, 3]]
for i in nums:
    print(Solution().productExceptSelf(i))
