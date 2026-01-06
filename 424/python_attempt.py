# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
#
# Return the length of the longest substring containing the same letter you can get after performing the above operations.


class Solution(object):
    def characterReplacement(self, s: str, k: int) -> int:
        count: dict[str, int] = {}
        longest_string_len: int = 0

        left_pointer_index: int = 0
        max_frequency: int = 0

        for right_pointer_index, right_letter in enumerate(s):
            count[right_letter] = 1 + count.get(right_letter, 0)
            if count[right_letter] > max_frequency:
                max_frequency = count[right_letter]

            while (right_pointer_index - left_pointer_index + 1) - max_frequency > k:
                count[s[left_pointer_index]] -= 1
                left_pointer_index += 1

            if (right_pointer_index - left_pointer_index + 1) > longest_string_len:
                longest_string_len = right_pointer_index - left_pointer_index + 1

        return longest_string_len


def test_cases():
    cur_solution = Solution()
    inputs = (
        {"s": "ABAB", "k": 2},
        {"s": "AABABBA", "k": 1},
        {"s": "AAAA", "k": 0},
        {"s": "AAAB", "k": 0},
    )
    outputs = [4, 4, 4, 3]

    all_passed = True

    for i in range(len(inputs)):
        result = 0
        try:
            result = cur_solution.characterReplacement(**inputs[i])
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
