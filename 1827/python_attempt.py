# You are given an integer array nums (0-indexed). In one operation, you can choose an element of the array and increment it by 1.
#
#     For example, if nums = [1,2,3], you can choose to increment nums[1] to make nums = [1,3,3].
#
# Return the minimum number of operations needed to make nums strictly increasing.
#
# An array nums is strictly increasing if nums[i] < nums[i+1] for all 0 <= i < nums.length - 1. An array of length 1 is trivially strictly increasing.


class Solution(object):
    def minOperations(self, nums):
        if len(nums) == 1:
            return 0
        previous_elm = nums[0] - 1
        # for elm in nums:
        #     if elm <= previous_elm:
        #         break
        #     previous_elm = elm
        # else:
        #     return 0

        total_operations_needed = 0
        previous_elm = nums[0] - 1
        for i, elm in enumerate(nums):
            if elm <= previous_elm:
                total_operations_needed += (previous_elm - elm) + 1
                nums[i] = previous_elm + 1
            previous_elm = nums[i]
        return total_operations_needed


def test_cases():
    cur_solution = Solution()
    try:
        pass
        assert cur_solution.minOperations([1, 1, 1]) == 3
        assert cur_solution.minOperations([1, 5, 2, 4, 1]) == 14
        assert cur_solution.minOperations([8]) == 0
    except Exception as e:
        print(f"Test unsuccessful: {e=}")
    else:
        print("All test cases passed.")


if __name__ == "__main__":
    test_cases()
    cur_solution = Solution()
    print(cur_solution.minOperations([1, 1, 1]))
