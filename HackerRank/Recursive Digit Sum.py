def superDigit(n, k):

    sum = 0
    digit_len = len(str(n))

    for num in str(n):
        sum += int(num)
    sum = sum * k
    digit_len = len(str(sum))

    if digit_len != 1:
        return superDigit(sum, 1)
    else:
        return sum


# superDigit(2, 3)
# print(superDigit(9875, 4))
# print(superDigit(148, 3))


# simpler version
def superDigit(n, k):

    sum = 0
    digits_len = len(str(n))

    if digits_len == 1:
        return n

    for num in str(n):
        sum += int(num)
    sum = sum * k
    return superDigit(sum, 1)


print(superDigit(9875, 4))
