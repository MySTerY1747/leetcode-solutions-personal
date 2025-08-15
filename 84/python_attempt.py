# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.


class Solution(object):
    def largestRectangleArea(self, heights: list[int]) -> int:
        #  INFO: First attempt:
        # heights_set: set[int] = set(heights)
        # max_area: int = 0
        #
        # for height in heights_set:
        #     max_consecutive: int = 0
        #     cur_consecutive: int = 0
        #     for value in heights:
        #         if value >= height:
        #             cur_consecutive += 1
        #             if cur_consecutive > max_consecutive:
        #                 max_consecutive = cur_consecutive
        #         else:
        #             cur_consecutive = 0
        #     cur_area: int = max_consecutive * height
        #     if cur_area > max_area:
        #         max_area = cur_area
        #
        # return max_area

        #  INFO: Second attempt
        stack: list[int] = []
        max_area: int = 0
        heights.append(0)
        heights_len: int = len(heights)

        for idx, elm in enumerate(heights):
            while stack and elm < heights[stack[-1]]:
                stack_top: int = stack.pop()
                left = stack[-1] if stack else -1
                width = idx - left - 1
                cur_area = heights[stack_top] * width
                if cur_area > max_area:
                    max_area = cur_area
            stack.append(idx)

        return max_area


def test_cases():
    cur_solution = Solution()
    inputs = (
        {"heights": [2, 1, 5, 6, 2, 3]},
        {"heights": [2, 4]},
        {"heights": [2, 1, 2]},
    )
    outputs = [10, 4, 3]

    all_passed = True

    for i in range(len(inputs)):
        result = 0
        try:
            result = cur_solution.largestRectangleArea(**inputs[i])
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
