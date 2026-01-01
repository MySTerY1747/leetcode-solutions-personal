# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
#
# Increment the large integer by one and return the resulting array of digits.


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for index in range(len(digits) - 1, -1, -1):
            digits[index] = (digits[index] + 1) % 10
            if digits[index] != 0:
                break
            if index == 0:
                digits.insert(0, 1)

        return digits


def test_cases():
    cur_solution = Solution()
    inputs = (
        {"digits": [1, 2, 3]},
        {"digits": [4, 3, 2, 1]},
        {"digits": [9]},
    )
    outputs = [[1, 2, 4], [4, 3, 2, 2], [1, 0]]

    all_passed = True

    for i in range(len(inputs)):
        result = 0
        try:
            result = cur_solution.plusOne(**inputs[i])
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
