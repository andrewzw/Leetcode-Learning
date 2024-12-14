class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        # Initialize a variable to count the number of flowers we can plant
        count = 0
        # Iterate through the flowerbed
        for i in range(len(flowerbed)):
            # Check if the current plot is empty
            if flowerbed[i] == 0:
                # Check if the previous and next plots are empty or if the current plot is at the edges
                if (i == 0 or flowerbed[i - 1] == 0) and (
                    i == len(flowerbed) - 1 or flowerbed[i + 1] == 0
                ):
                    # Plant a flower and update the count
                    flowerbed[i] = 1
                    count += 1

        # Check if the count is greater than or equal to n
        return count >= n


flowerbed = [1, 0, 0, 0, 1]
n = [1, 2]

for i in n:
    print(Solution().canPlaceFlowers(flowerbed, i))
