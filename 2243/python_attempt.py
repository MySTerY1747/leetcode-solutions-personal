# You are given a string s consisting of digits and an integer k.
#
# A round can be completed if the length of s is greater than k. In one round, do the following:
#
#     Divide s into consecutive groups of size k such that the first k characters are in the first group, the next k characters are in the second group, and so on. Note that the size of the last group can be smaller than k.
#     Replace each group of s with a string representing the sum of all its digits. For example, "346" is replaced with "13" because 3 + 4 + 6 = 13.
#     Merge consecutive groups together to form a new string. If the length of the string is greater than k, repeat from step 1.
#
# Return s after all rounds have been completed.


class Solution(object):
    def digitSum(self, s, k):
        sublist = []
        if len(s) >= k:
            for i in range(0, len(s), 3):
                sublist.append(s[i : i + 3])
        summed_list = []
        for elm in sublist:
            summed_list.append(str(sum([int(a) for a in elm])))
        return "".join(summed_list)


def test_cases():
    cur_solution = Solution()
    try:
        assert cur_solution.digitSum(s="11111222223", k=3) == "135"
        assert cur_solution.digitSum(s="00000000", k=3) == "000"
    except Exception as e:
        print(f"Test unsuccessful: {e=}")
    else:
        print("All test cases passed.")


if __name__ == "__main__":
    test_cases()
    cur_solution = Solution()
    print(cur_solution.digitSum(s="11111222223", k=3))
