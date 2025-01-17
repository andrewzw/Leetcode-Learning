def isBalanced(s):
    # Write your code here
    if len(s) % 2 != 0:
        return "NO"

    brackets = {"{": "}", "[": "]", "(": ")"}

    stack = []

    for char in s:

        if char in "{[(":
            stack.append(char)
        elif char in "}])":
            if not stack:
                return "NO"
            if char != brackets[stack.pop()]:
                return "NO"

    if not stack:
        return "YES"
    else:
        return "NO"


tests = {
    "test0": ["{[()]}", "YES"],
    "test1": ["{[(])}", "NO"],
    "test2": ["{{[[(())]]}}", "YES"],
    "test3": ["{{([])}}", "YES"],
    "test4": ["{{)[](}}", "NO"],
    "test5": ["{(([])[])[]}", "YES"],
    "test6": ["{(([])[])[]]}", "NO"],
    "test7": ["{(([])[])[]}[]", "YES"],
}

failed = 0
for key in tests:

    output = isBalanced(tests[key][0])
    if output == tests[key][1]:
        print(key + " is Passed\n")
    else:
        failed += 1
        print(
            f"{tests[key][0]}\n{key} Failed Expected: {tests[key][1]} but got: {output}\n"
        )

if failed == 0:
    print("All test cases passed")
else:
    print(f"Failed {failed} / {len(tests)} test cases ")
