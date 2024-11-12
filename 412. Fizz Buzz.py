class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = []
        for i in range(1, n + 1):
            result = ""
            if i % 3 == 0:
                result += "Fizz"

            if i % 5 == 0:
                result += "Buzz"

            if result == "":
                result = str(i)

            answer.append(result)

        return answer


n = [3, 5, 15]
for i in n:
    print(Solution().fizzBuzz(i))
