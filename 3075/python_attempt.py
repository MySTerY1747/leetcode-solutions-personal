# You are given an array happiness of length n, and a positive integer k.
#
# There are n children standing in a queue, where the ith child has happiness value happiness[i]. You want to select k children from these n children in k turns.
#
# In each turn, when you select a child, the happiness value of all the children that have not been selected till now decreases by 1. Note that the happiness value cannot become negative and gets decremented only if it is positive.
#
# Return the maximum sum of the happiness values of the selected children you can achieve by selecting k children.


class Solution(object):
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        happiness_sum: int = 0
        happiness.sort(reverse=True)

        for iter in range(k):
            happiness_sum += max(happiness[iter] - iter, 0)

        return happiness_sum


def test_cases():
    cur_solution = Solution()
    inputs = (
        {"happiness": [1, 2, 3], "k": 2},
        {"happiness": [1, 1, 1, 1], "k": 2},
        {"happiness": [2, 3, 4, 5], "k": 1},
    )
    outputs = [4, 1, 5]

    all_passed = True

    for i in range(len(inputs)):
        result = 0
        try:
            result = cur_solution.maximumHappinessSum(**inputs[i])
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
