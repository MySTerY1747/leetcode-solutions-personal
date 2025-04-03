# You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.
#
# Notice that x does not have to be an element in nums.
#
# Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.


class Solution(object):
    def specialArray(self, nums):
        for i in range(max(nums) + 1):
            continue_flag = False
            cur_total = 0
            for number in nums:
                if number >= i:
                    cur_total += 1
                    if cur_total > i:
                        continue_flag = True
                        break
            if continue_flag:
                continue
            if i == cur_total:
                return i
        return -1


def test_cases():
    cur_solution = Solution()
    try:
        assert cur_solution.specialArray([3, 5]) == 2
        assert cur_solution.specialArray([0, 0]) == -1
        assert cur_solution.specialArray([0, 4, 3, 0, 4]) == 3
    except Exception as e:
        print(f"Test unsuccessful: {e=}")
    else:
        print("All test cases passed.")


if __name__ == "__main__":
    test_cases()
    cur_solution = Solution()
    print(cur_solution.specialArray([3, 5]))
