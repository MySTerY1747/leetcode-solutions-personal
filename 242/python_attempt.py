#  Given two strings s and t, return true if t is an of s, and false otherwise.


class Solution(object):
    def isAnagram(self, s, t):
        #  convert s to dictionary
        s_dict = {}
        t_dict = {}
        for letter in s:
            s_dict[letter] = s_dict.get(letter, 0) + 1
        for letter in t:
            t_dict[letter] = t_dict.get(letter, 0) + 1

        return s_dict == t_dict


def test_cases():
    cur_solution = Solution()
    try:
        assert cur_solution.isAnagram(s="anagram", t="nagaram") is True
        assert cur_solution.isAnagram(s="rat", t="car") is False
    except Exception as e:
        print(f"Test unsuccessful: {e=}")
    else:
        print("All test cases passed.")


if __name__ == "__main__":
    test_cases()
