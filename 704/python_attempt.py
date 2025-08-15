# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
#
# You must write an algorithm with O(log n) runtime complexity.


class Solution(object):
    def search(self, nums: list[int], target: int) -> int:
        left: int = 0
        right: int = len(nums) - 1

        while left <= right:
            mid: int = (right + left) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return -1


def test_cases():
    cur_solution = Solution()
    inputs = (
        {"nums": [-1, 0, 3, 5, 9, 12], "target": 9},
        {"nums": [-1, 0, 3, 5, 9, 12], "target": 2},
        {"nums": [5], "target": 5},
    )
    outputs = [4, -1, 0]

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
