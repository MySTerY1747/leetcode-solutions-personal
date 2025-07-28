# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.


class Solution(object):
    def isValid(self, s):
        closing_brackets = {")": "(", "}": "{", "]": "["}
        stack = []
        bracket_count = 0
        if len(s) % 2 != 0:
            return False
        for bracket in s:
            if bracket in closing_brackets:
                if len(stack) == 0 or stack.pop() != closing_brackets[bracket]:
                    return False
                bracket_count -= 1
            else:
                stack.append(bracket)
                bracket_count += 1
        return bracket_count == 0


def test_cases():
    cur_solution = Solution()
    inputs = (
        {"s": "()"},
        {"s": "()[]{}"},
        {"s": "(]"},
        {"s": "([])"},
        {"s": "([)]"},
    )
    outputs = [True, True, False, True, False]

    all_passed = True

    for i in range(len(inputs)):
        try:
            result = cur_solution.isValid(**inputs[i])
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
