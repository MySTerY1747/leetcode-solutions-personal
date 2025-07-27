# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.


class Solution(object):
    def trap(self, height):
        rainwater_area = 0
        left_index = 0
        left_max = 0
        right_index = len(height) - 1
        right_max = 0
        while left_index < right_index and height[left_index] == 0:
            left_index += 1
        left_max = height[left_index]  #  first non-zero value

        while left_index < right_index and height[right_index] == 0:
            right_index -= 1
        right_max = height[right_index]

        while left_index < right_index:
            if left_max <= right_max:
                left_index += 1
                while left_index < right_index and height[left_index] < left_max:
                    rainwater_area += left_max - height[left_index]
                    left_index += 1
                left_max = max(left_max, height[left_index])
            else:
                right_index -= 1
                while left_index < right_index and height[right_index] < right_max:
                    rainwater_area += right_max - height[right_index]
                    right_index -= 1
                right_max = max(right_max, height[right_index])

        return rainwater_area


def test_cases():
    cur_solution = Solution()
    inputs = (
        {"height": [1, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]},
        {"height": [4, 2, 0, 3, 2, 5]},
        {"height": [4, 2, 3]},
    )
    outputs = [6, 9, 1]

    all_passed = True

    for i in range(len(inputs)):
        try:
            result = cur_solution.trap(**inputs[i])
            assert result == outputs[i]
        except AssertionError:
            all_passed = False
            input_str = ", ".join(
                [f"{key}={value}" for key, value in inputs[i].items()]
            )
            print(
                f"• 🟥 Test {i} failed: Input: {input_str}. Expected: {outputs[i]}, Got: {result}\n"
            )
        except Exception as e:
            all_passed = False
            print(f"❗️Unexpected error on test {i}: {e}")

    if all_passed:
        print("✅ All test cases passed!")


if __name__ == "__main__":
    test_cases()
