# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.


class Solution(object):
    def searchInsert(self, nums, target):
        middle_index = len(nums) // 2
        print(nums, middle_index)
        if len(nums) == 1:
            return 1 if target > nums[0] else 0
        if nums[middle_index] == target:
            return middle_index
        elif target < nums[middle_index]:
            return self.searchInsert(nums[:middle_index], target)
        else:
            return middle_index + self.searchInsert(nums[middle_index:], target)


def test_cases():
    cur_solution = Solution()
    try:
        assert cur_solution.searchInsert(nums=[1, 3, 5, 6], target=5) == 5
        assert cur_solution.searchInsert(nums=[1, 3, 5, 6], target=2) == 1
        assert cur_solution.searchInsert(nums=[1, 3, 5, 6], target=7) == 4
    except Exception as e:
        print(f"Test unsuccessful: {e=}")
    else:
        print("All test cases passed.")


if __name__ == "__main__":
    test_cases()
    cur_solution = Solution()
    # print(cur_solution.sumOddLengthSubarrays([1, 4, 2, 5, 3]))
