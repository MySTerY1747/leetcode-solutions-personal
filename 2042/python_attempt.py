# A sentence is a list of tokens separated by a single space with no leading or trailing spaces. Every token is either a positive number consisting of digits 0-9 with no leading zeros, or a word consisting of lowercase English letters.
#
#     For example, "a puppy has 2 eyes 4 legs" is a sentence with seven tokens: "2" and "4" are numbers and the other tokens such as "puppy" are words.
#
# Given a string s representing a sentence, you need to check if all the numbers in s are strictly increasing from left to right (i.e., other than the last number, each number is strictly smaller than the number on its right in s).
#
# Return true if so, or false otherwise.


class Solution(object):
    def areNumbersAscending(self, s):
        # previous_num = -1
        # cur_num = ""
        # for i, character in enumerate(s):
        #     if character not in cur_num:
        #         cur_num = ""
        #         if character in "0123456789":
        #             for subcharacter in s[i:]:
        #                 if subcharacter in "0123456789":
        #                     cur_num += subcharacter
        #                 else:
        #                     break
        #             if int(cur_num) <= previous_num:
        #                 print(f"{cur_num=}, {previous_num=}")
        #                 return False
        #             previous_num = int(cur_num)
        # return True
        new_s = filter(lambda a: a.isdigit(), s.split(" "))
        previous_num = -1
        for num in new_s:
            if int(num) <= int(previous_num):
                return False
            previous_num = num
        return True


def test_cases():
    cur_solution = Solution()
    try:
        assert (
            cur_solution.areNumbersAscending(
                "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
            )
            is True
        )
        assert cur_solution.areNumbersAscending("hello world 5 x 5") is False
        assert (
            cur_solution.areNumbersAscending(
                "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"
            )
            is False
        )
    except Exception as e:
        print(f"Test unsuccessful: {e=}")
    else:
        print("All test cases passed.")


if __name__ == "__main__":
    test_cases()
    cur_solution = Solution()
    print(cur_solution.areNumbersAscending("1 box and 3 and 4 and 6 and 12"))
