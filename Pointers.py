arr1 = [2, 1, 5, 6, 3]
arr2 = [7, 2, 1, 7, 8]


def findMax(arr):
    max = 0
    for num in arr:
        if num > max:
            max = num
    print(max)


findMax(arr1)


def findMaxArrs(arr1, arr2):
    max = 0
    fromArr = None
    for num in arr1:
        if num > max:
            max = num
            fromArr = arr1
    for num in arr2:
        if num > max:
            max = num
            fromArr = arr2
    print(max, fromArr)


findMaxArrs(arr1, arr2)


def findMaxSum(arr):
    n = len(arr)
    arr.sort()
    maxSum = arr[n - 2] + arr[n - 1]
    print(maxSum, arr)


findMaxSum(arr2)


def twoPointer(arr):
    arr.sort()
    n = len(arr)
    i = 0
    j = n - 1
    print(arr)
    while i < j:
        print(arr[i], arr[j])
        i += 1
        j -= 1


twoPointer(arr1)


def encodedWord(s):
    s = s.split(" ")
    joined = ""

    for word in s:
        joined += f"{len(word)}#{word}"
    print("Encoded:", joined)
    return joined


def decodedWord(s):
    curr_word = ""
    count = 0

    for char in s:
        if char.isdigit():
            count = int(char)

        if char.isalpha():
            curr_word += char
            count -= 1
            if count == 0:
                curr_word = f"{curr_word} "

    print("Decoded:", curr_word)


s = "hello ken kk"
decodedWord(encodedWord(s))
