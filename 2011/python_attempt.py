# There is a programming language with only four operations and one variable X:
#
#     ++X and X++ increments the value of the variable X by 1.
#     --X and X-- decrements the value of the variable X by 1.
#
# Initially, the value of X is 0.
#
# Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.


class Solution(object):
    def finalValueAfterOperations(self, operations):
        cur_value = 0
        for operation in operations:
            if "-" in operation:
                cur_value -= 1
            else:
                cur_value += 1
        return cur_value


def test_cases():
    cur_solution = Solution()
    try:
        assert cur_solution.finalValueAfterOperations(["--X", "X++", "X++"]) == 1
        assert cur_solution.finalValueAfterOperations(["++X", "++X", "X++"]) == 3
        assert cur_solution.finalValueAfterOperations(["X++", "++X", "--X", "X--"]) == 0
    except Exception as e:
        print(f"Test unsuccessful: {e=}")
    else:
        print("All test cases passed.")


if __name__ == "__main__":
    test_cases()
