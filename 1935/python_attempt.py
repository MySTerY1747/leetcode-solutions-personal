# There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.
#
# Given a string text of words separated by a single space (no leading or trailing spaces) and a string brokenLetters of all distinct letter keys that are broken, return the number of words in text you can fully type using this keyboard.


class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        return sum(
            [
                1
                for word in text.split(" ")
                if not (
                    any([True if letter in brokenLetters else False for letter in word])
                )
            ]
        )


def test_cases():
    cur_solution = Solution()
    try:
        assert cur_solution.canBeTypedWords("hello world", "ad") == 1
        assert cur_solution.canBeTypedWords("leet code", "lt") == 1
        assert cur_solution.canBeTypedWords("leet code", "e") == 0
    except Exception as e:
        print(f"Test unsuccessful: {e=}")
    else:
        print("All test cases passed.")


if __name__ == "__main__":
    test_cases()
    cur_solution = Solution()
