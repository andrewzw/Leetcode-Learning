def stockPairs(stocksProfit, target):
    # Write your code here
    stocksProfit.sort()
    n = len(stocksProfit)
    left, right = 0, n - 1
    pairs = set()
    # print(stocksProfit)
    while left < right:
        sum = stocksProfit[left] + stocksProfit[right]
        # print((stocksProfit[left], stocksProfit[right]))
        if sum == target:
            pairs.add((stocksProfit[left], stocksProfit[right]))
            left += 1
            right -= 1
        elif sum < target:
            left += 1
        else:
            right -= 1

    print(len(pairs), ":", pairs)


stockProfit = [5, 7, 9, 13, 11, 6, 6, 3, 3]
target = 12


stockPairs(stockProfit, target)
