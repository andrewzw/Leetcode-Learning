#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n number of towers
#  2. INTEGER m height of tower

# x height of tower
# y reduce to

# y >= 1
# x > y
# y % x == 0   y evenly divides x
# lose when unable to move

# player 1 wins returns 1
# player 2 wins returns 2


def towerBreakers(n, m):
    # Write your code here
    # n = number of towers
    # m = height of tower
    if n % 2 == 0 or m == 1:
        return 2
    return 1


# Starting
# #
# #
# #
# #

# P1 takes 3 from tower 2

#
#
#
# #

# P2 takes 3 from tower 1

# #

# P1 loses when height(m) is 1

# #


print((2, 2), towerBreakers(2, 2))  # 2
print((1, 4), towerBreakers(1, 4))  # 1

print((1, 7), towerBreakers(1, 7))  # 1
print((3, 7), towerBreakers(3, 7))  # 1
