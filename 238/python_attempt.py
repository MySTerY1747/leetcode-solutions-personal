# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without using the division operation.


class Solution(object):
    def productExceptSelf(self, nums):
        final_result = []
        prefix = 1
        suffix = 1
        prod_without_zero = 1
        nums_without_zero: list = nums.copy()
        nums_without_zero.remove(0)
        for num in nums:
            suffix *= num
        for num in nums_without_zero:
            prod_without_zero *= num
        print(f"{prod_without_zero=}")

        for i, num in enumerate(nums):
            if i != 0:
                prefix *= nums[i - 1]
            if nums[i] != 0:
                suffix /= nums[i]

            if num == 0:
                final_result.append(prod_without_zero)
            else:
                final_result.append(int(prefix * suffix))
        return final_result


def test_cases():
    cur_solution = Solution()
    try:
        assert cur_solution.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
        assert cur_solution.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    except Exception as e:
        print(f"Test unsuccessful: {e=}")
    else:
        print("All test cases passed.")


if __name__ == "__main__":
    test_cases()
    cur_solution = Solution()
    print(cur_solution.productExceptSelf([-1, 1, 0, -3, 3]))
