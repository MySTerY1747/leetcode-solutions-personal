# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
#
#     [4,5,6,7,0,1,2] if it was rotated 4 times.
#     [0,1,2,4,5,6,7] if it was rotated 7 times.
#
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
#
# Given the sorted rotated array nums of unique elements, return the minimum element of this array.
#
# You must write an algorithm that runs in O(log n) time.


class Solution(object):
    def findMin(self, nums: list[int]) -> int:
        left: int = 0
        right: int = len(nums) - 1
        mid: int = 0

        while left < right:
            mid: int = (left + right) // 2
            if left == mid:
                return min(nums[left], nums[left + 1])
            if nums[mid] <= nums[left]:  #  there is a break in the left half
                right = mid
            elif nums[mid] >= nums[right]:  #  there is a break in the right half
                left = mid
            else:
                return nums[0]  #  the list is already sorted with no rotation

        return nums[0] if len(nums) == 1 else nums[mid + 1]


def test_cases():
    cur_solution = Solution()
    inputs = (
        {"nums": [3, 4, 5, 1, 2]},
        {"nums": [4, 5, 6, 7, 0, 1, 2]},
        {"nums": [11, 13, 15, 17]},
        {"nums": [1, 2]},
    )
    outputs = [1, 0, 11, 1]

    all_passed = True

    for i in range(len(inputs)):
        result = 0
        try:
            result = cur_solution.findMin(**inputs[i])
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
