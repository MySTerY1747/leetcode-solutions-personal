# You are given an m x n integer matrix matrix with the following two properties:
#
#     Each row is sorted in non-decreasing order.
#     The first integer of each row is greater than the last integer of the previous row.
#
# Given an integer target, return true if target is in matrix or false otherwise.
#
# You must write a solution in O(log(m * n)) time complexity.


class Solution(object):
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        def search(nums: list[int], target: int) -> int:
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

        left_matrix: int = 0
        right_matrix: int = len(matrix) - 1
        while left_matrix <= right_matrix:
            mid: int = (left_matrix + right_matrix) // 2
            if target < matrix[mid][0]:
                right_matrix = mid - 1
            elif target > matrix[mid][-1]:
                left_matrix = mid + 1
            else:
                return False if search(matrix[mid], target) == -1 else True

        return False


def test_cases():
    cur_solution = Solution()
    inputs = (
        {"matrix": [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], "target": 3},
        {"matrix": [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], "target": 13},
    )
    outputs = [True, False]

    all_passed = True

    for i in range(len(inputs)):
        result = 0
        try:
            result = cur_solution.searchMatrix(**inputs[i])
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
