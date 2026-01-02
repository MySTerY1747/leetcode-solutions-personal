# Given a string s, find the length of the longest substring without duplicate characters.


class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest: int = 0
        cur_streak: int = 0
        last_index_of_char: dict[str, int] = {}
        index: int = 0
        cur_start: int = 0
        for index, letter in enumerate(s):
            if last_index_of_char.get(letter, -1) < cur_start:
                cur_streak += 1
                last_index_of_char[letter] = index
                if cur_streak > longest:
                    longest = cur_streak
                index += 1
            else:
                cur_streak = index - last_index_of_char[letter]
                cur_start = last_index_of_char[letter] + 1
                last_index_of_char[letter] = index
                index += 1
        if cur_streak > longest:
            longest = cur_streak
        return longest


def test_cases():
    cur_solution = Solution()
    inputs = (
        {"s": "abcabcbb"},
        {"s": "bbbbb"},
        {"s": "pwwkew"},
        {"s": "aab"},
        {"s": "dvdf"},
        {"s": "tmmzuxt"},
        {"s": " "},
        {"s": "au"},
    )
    outputs = [3, 1, 3, 2, 3, 5, 1, 2]

    all_passed = True

    for i in range(len(inputs)):
        result = 0
        try:
            result = cur_solution.lengthOfLongestSubstring(**inputs[i])
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
