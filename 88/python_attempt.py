# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
#
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

from typing import List, Optional


class Solution(object):
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1_copy = nums1.copy()
        index_0: int = 0
        index_1: int = 0
        index_2: int = 0

        while (index_1 < m) or (index_2 < n):
            if index_1 >= m:
                print("Case 1")
                nums1[index_0] = nums2[index_2]
                index_0 += 1
                index_2 += 1
            elif index_2 >= n:
                print("Case 2")
                nums1[index_0] = nums1_copy[index_1]
                index_0 += 1
                index_1 += 1
            else:
                print("Case 3")
                minimum = min(nums1_copy[index_1], nums2[index_2])
                nums1[index_0] = minimum
                index_0 += 1
                if minimum == nums1_copy[index_1]:
                    index_1 += 1
                else:
                    index_2 += 1


def test_cases():
    cur_solution = Solution()
    inputs = (
        {"nums1": [1, 2, 3, 0, 0, 0], "m": 3, "nums2": [2, 5, 6], "n": 3},
        {"nums1": [1], "m": 1, "nums2": [], "n": 0},
        {"nums1": [0], "m": 0, "nums2": [1], "n": 1},
    )
    outputs = [[1, 2, 2, 3, 5, 6], [1], [1]]

    all_passed = True

    for i in range(len(inputs)):
        result = 0
        try:
            result = cur_solution.merge(**inputs[i])
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
