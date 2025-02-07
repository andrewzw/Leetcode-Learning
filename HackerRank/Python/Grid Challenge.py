def gridChallenge(grid):
    # Write your code here

    sorted_grid = []
    for row in grid:
        sorted_grid.append(sorted(row))

    for col in range(len(sorted_grid[0])):
        for row in range(1, len(sorted_grid)):
            if sorted_grid[row - 1][col] > sorted_grid[row][col]:
                return "NO"

    return "YES"


# grid = ["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]
# grid = ["ebacd", "fghij"]


def gridChallenge(grid):
    # Write your code here
    sorted_grid = []
    n = len(grid)  # num of rows
    m = len(grid[0])  # length of col)

    for row in grid:
        sorted_grid.append(sorted(row))

    for row in range(n - 1):
        for col in range(m):
            if sorted_grid[row][col] > sorted_grid[row + 1][col]:
                return "NO"
    return "YES"


grid = ["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]  # "YES"
grid = ["abc", "lmp", "qrt"]  # "YES"
print(gridChallenge(grid))
