#  Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.


class Solution(object):
    def titleToNumber(self, columnTitle):
        total = 0
        for index, letter in enumerate(columnTitle[::-1]):
            total += (ord(letter) - 64) * (26**index)
        return total


def test_cases():
    cur_solution = Solution()
    try:
        assert cur_solution.titleToNumber("A") == 1
        assert cur_solution.titleToNumber("AB") == 28
        assert cur_solution.titleToNumber("ZY") == 701
    except Exception as e:
        print(f"Test unsuccessful: {e=}")
    else:
        print("All test cases passed.")


if __name__ == "__main__":
    test_cases()
    solution = Solution()
    print(solution.titleToNumber("BD"))
