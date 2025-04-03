# Given a 0-indexed integer array nums, return the smallest index i of nums such that i mod 10 == nums[i], or -1 if such index does not exist.
#
# x mod y denotes the remainder when x is divided by y.


class Solution(object):
    def smallestEqual(self, nums):
        for i, elm in enumerate(nums):
            if i % 10 == elm:
                return i
        return -1


def test_cases():
    try:
        cur_solution = Solution()
        assert cur_solution.smallestEqual([0, 1, 2]) == 0
        assert cur_solution.smallestEqual([4, 3, 2, 1]) == 2
        assert cur_solution.smallestEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == -1
    except Exception as e:
        print(f"Something went wrong! {e}")
    else:
        print("All test cases passed successfully.")


if __name__ == "__main__":
    test_cases()
