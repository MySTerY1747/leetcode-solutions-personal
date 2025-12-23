# Given a string s consisting of words and spaces, return the length of the last word in the string.
#
# A word is a maximal consisting of non-space characters only.


class Solution(object):
    def lengthOfLastWord(self, s):
        filtered_s = s.split(" ")
        for word in filtered_s[::-1]:
            if len(word) != 0:
                return len(word)


def test_cases():
    cur_solution = Solution()
    try:
        assert cur_solution.lengthOfLastWord(s="Hello World") == 5
        assert cur_solution.lengthOfLastWord(s="   fly me   to   the moon  ") == 4
        assert cur_solution.lengthOfLastWord(s="luffy is still joyboy") == 6

    except Exception as e:
        print(f"Test unsuccessful: {e=}")
    else:
        print("All test cases passed.")


if __name__ == "__main__":
    test_cases()
