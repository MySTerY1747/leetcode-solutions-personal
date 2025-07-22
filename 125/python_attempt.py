# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.


class Solution(object):
    def isPalindrome(self, s):
        edited_s = "".join([letter.lower() for letter in s if letter.isalnum()])
        return edited_s == edited_s[::-1]


def test_cases():
    cur_solution = Solution()
    try:
        assert cur_solution.isPalindrome(s="A man, a plan, a canal: Panama") is True
        assert cur_solution.isPalindrome(s="race a car") is False
        assert cur_solution.isPalindrome(s=" ") is True

    except Exception as e:
        print(f"Test unsuccessful: {e=}")
    else:
        print("All test cases passed.")


if __name__ == "__main__":
    test_cases()
