# There is an integer array nums sorted in ascending order (with distinct values).
#
# Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].
#
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
#
# You must write an algorithm with O(log n) runtime complexity


class Solution(object):
    def search(self, nums: list[int], target: int) -> int:
        left: int = 0
        right: int = len(nums) - 1
        mid: int = 0

        while left <= right:
            mid: int = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                #  left half is sorted
                if nums[left] <= target <= nums[mid]:
                    right: int = mid - 1
                else:
                    left: int = mid + 1
            else:
                #  right half is sorted
                if nums[mid] <= target <= nums[right]:
                    left: int = mid + 1
                else:
                    right: int = mid - 1
        return -1


def test_cases():
    cur_solution = Solution()
    inputs = (
        {"nums": [4, 5, 6, 7, 0, 1, 2], "target": 0},
        {"nums": [4, 5, 6, 7, 0, 1, 2], "target": 3},
        {"nums": [1], "target": 0},
        {"nums": [1], "target": 1},
    )
    outputs = [4, -1, -1, 0]

    all_passed = True

    for i in range(len(inputs)):
        result = 0
        try:
            result = cur_solution.search(**inputs[i])
            assert result == outputs[i]
        except AssertionError:
            all_passed = False
            input_str = ", ".join(
                [f"{key}={value}" for key, value in inputs[i].items()]
            )
            print(
                f"• 🟥 Test {i + 1} failed: Input: {input_str}. Expected: {outputs[i]}, Got: {result}\n"
            )
        except Exception as e:
            all_passed = False
            print(f"❗️Unexpected error on test {i + 1}: {e}")

    if all_passed:
        print("✅ All test cases passed!")


if __name__ == "__main__":
    test_cases()
