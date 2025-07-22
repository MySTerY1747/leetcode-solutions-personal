# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
#
# You must write an algorithm that runs in O(n) time.


class Solution(object):
    def longestConsecutive(self, nums):
        num_set = set(nums)
        longest_sequence = 0

        for num in num_set:
            if num - 1 not in num_set:
                cur_streak = 1

                while num + 1 in num_set:
                    cur_streak += 1
                    num += 1
                if cur_streak > longest_sequence:
                    longest_sequence = cur_streak
                cur_streak = 0

        return longest_sequence


def test_cases():
    cur_solution = Solution()
    try:
        assert cur_solution.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]) == 4
        assert cur_solution.longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
        assert cur_solution.longestConsecutive(nums=[1, 0, 1, 2]) == 3

    except Exception as e:
        print(f"Test unsuccessful: {e=}")
    else:
        print("All test cases passed.")


if __name__ == "__main__":
    test_cases()
