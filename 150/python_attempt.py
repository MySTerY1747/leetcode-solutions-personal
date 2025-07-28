# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
#
# Evaluate the expression. Return an integer that represents the value of the expression.
#
# Note that:
#
#     The valid operators are '+', '-', '*', and '/'.
#     Each operand may be an integer or another expression.
#     The division between two integers always truncates toward zero.
#     There will not be any division by zero.
#     The input represents a valid arithmetic expression in a reverse polish notation.
#     The answer and all the intermediate calculations can be represented in a 32-bit integer.


class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        operators = {"+", "-", "*", "/"}
        for token in tokens:
            if token in operators:
                val2 = stack.pop()
                val1 = stack.pop()
                if token == "+":
                    stack.append(val1 + val2)
                elif token == "-":
                    stack.append(val1 - val2)
                elif token == "*":
                    stack.append(val1 * val2)
                elif token == "/":
                    stack.append(int(val1 / val2))
            else:
                stack.append(int(token))
        return stack[-1]


def test_cases():
    cur_solution = Solution()
    inputs = (
        {"tokens": ["2", "1", "+", "3", "*"]},
        {"tokens": ["4", "13", "5", "/", "+"]},
        {
            "tokens": [
                "10",
                "6",
                "9",
                "3",
                "+",
                "-11",
                "*",
                "/",
                "*",
                "17",
                "+",
                "5",
                "+",
            ]
        },
    )
    outputs = [9, 6, 22]

    all_passed = True

    for i in range(len(inputs)):
        result = 0
        try:
            result = cur_solution.evalRPN(**inputs[i])
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
