# You are given coordinates, a string that represents the coordinates of a square of the chessboard. Below is a chessboard for your reference.
#
# Return true if the square is white, and false if the square is black.
#
# The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first, and the number second.


class Solution(object):
    def squareIsWhite(self, coordinates):
        if coordinates[0] in "aceg":
            return int(coordinates[1]) % 2 == 0
        return int(coordinates[1]) % 2 == 1


def test_cases():
    cur_solution = Solution()
    try:
        assert cur_solution.squareIsWhite("a1") is False
        assert cur_solution.squareIsWhite("h3") is True
        assert cur_solution.squareIsWhite("c7") is False
    except Exception as e:
        print(f"Test unsuccessful: {e=}")
    else:
        print("All test cases passed.")


if __name__ == "__main__":
    test_cases()
    cur_solution = Solution()
    print(cur_solution.squareIsWhite("a1"))
