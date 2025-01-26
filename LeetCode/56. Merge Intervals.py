from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        results = []
        intervals.sort(
            key=lambda interval: interval[0]
        )  # sort using first item of interval as sorting key

        for item in intervals:
            # if results is empty
            # or if last item'ending is less than first item's starting
            if not results or results[-1][1] < item[0]:
                results.append(item)

            else:
                # manipulate last item using starting of previous item and max of ending of both items
                results[-1] = [results[-1][0], max(results[-1][1], item[1])]

        return results


merged = Solution()
print(merged.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(merged.merge([[1, 4], [4, 5]]))
print(merged.merge([[1, 4], [0, 4]]))
