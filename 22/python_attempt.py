# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


class Solution(object):
    # INFO: First version:
    #
    # def generateParenthesis(self, n: int) -> list[str]:
    #     output: list[str] = []
    #
    #     def continueChain(
    #         input_string: str, parentheses_open: int, parentheses_closed: int
    #     ) -> None:
    #         if (parentheses_open == n) and (parentheses_closed == n):
    #             output.append(input_string)
    #             return
    #         if parentheses_open < n:
    #             continueChain(
    #                 input_string + "(", parentheses_open + 1, parentheses_closed
    #             )
    #         if (parentheses_closed < n) and (parentheses_open > parentheses_closed):
    #             continueChain(
    #                 input_string + ")", parentheses_open, parentheses_closed + 1
    #             )
    #
    #     continueChain("", 0, 0)
    #
    #     return output

    # INFO: Second version:

    def generateParenthesis(self, n: int) -> list[str]:
        output: list[str] = []
        stack: list[str] = []

        def continueChain(parentheses_opened: int, parentheses_closed: int) -> None:
            if (parentheses_opened == n) and (parentheses_closed == n):
                output.append("".join(stack))
                return
            if parentheses_opened < n:
                stack.append("(")
                continueChain(parentheses_opened + 1, parentheses_closed)
                stack.pop()
            if (parentheses_closed < n) and (parentheses_opened > parentheses_closed):
                stack.append(")")
                continueChain(parentheses_opened, parentheses_closed + 1)
                stack.pop()

        continueChain(0, 0)

        return output


def test_cases():
    cur_solution = Solution()
    inputs = (
        {"n": 3},
        {"n": 1},
    )
    outputs = [["((()))", "(()())", "(())()", "()(())", "()()()"], ["()"]]

    all_passed = True

    for i in range(len(inputs)):
        result = 0
        try:
            result = cur_solution.generateParenthesis(**inputs[i])
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
