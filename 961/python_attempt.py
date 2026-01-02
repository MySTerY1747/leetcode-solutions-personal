# You are given an integer array nums with the following properties:
#
#     nums.length == 2 * n.
#     nums contains n + 1 unique elements.
#     Exactly one element of nums is repeated n times.
#
# Return the element that is repeated n times.


class Solution(object):
    def repeatedNTimes(self, nums: list[int]) -> int:
        visited_set: set[int] = set()
        for num in nums:
            if num in visited_set:
                return num
            visited_set.add(num)
        return -1  #  error: elm not present


def test_cases():
    cur_solution = Solution()
    inputs = (
        {"nums": [1, 2, 3, 3]},
        {"nums": [2, 1, 2, 5, 3, 2]},
        {"nums": [5, 1, 5, 2, 5, 3, 5, 4]},
    )
    outputs = [3, 2, 5]

    all_passed = True

    for i in range(len(inputs)):
        result = 0
        try:
            result = cur_solution.repeatedNTimes(**inputs[i])
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
