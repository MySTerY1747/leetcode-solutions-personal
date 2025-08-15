# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.


class Solution(object):
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        total_length: int = len(temperatures)
        output: list[int] = [0] * total_length
        stack: list[int] = []

        for idx in range(total_length - 1, -1, -1):
            elm: int = temperatures[idx]

            if not stack:
                stack.append(idx)
            elif elm < temperatures[stack[-1]]:
                output[idx] = stack[-1] - idx
                stack.append(idx)
            else:
                while (stack) and temperatures[stack[-1]] <= elm:
                    stack.pop()
                if not stack:
                    stack.append(idx)
                elif elm < temperatures[stack[-1]]:
                    output[idx] = stack[-1] - idx
                    stack.append(idx)

        return output


def test_cases():
    cur_solution = Solution()
    inputs = (
        {"temperatures": [73, 74, 75, 71, 69, 72, 76, 73]},
        {"temperatures": [30, 40, 50, 60]},
        {"temperatures": [30, 60, 90]},
        {"temperatures": [89, 62, 70, 58, 47, 47, 46, 76, 100, 70]},
    )
    outputs = [
        [1, 1, 4, 2, 1, 1, 0, 0],
        [1, 1, 1, 0],
        [1, 1, 0],
        [8, 1, 5, 4, 3, 2, 1, 1, 0, 0],
    ]

    all_passed = True

    for i in range(len(inputs)):
        result = 0
        try:
            result = cur_solution.dailyTemperatures(**inputs[i])
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
