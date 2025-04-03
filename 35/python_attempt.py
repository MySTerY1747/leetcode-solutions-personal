# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.


class Solution(object):
    def searchInsert(self, nums, target):
        middle = len(nums) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            self.searchInsert(nums[:middle], target)
        else:
            self.searchInsert(nums[middle:], target)


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
