# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
#
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


class Solution(object):
    def isSubsequence(self, s: str, t: str) -> bool:
        idx: int = 0
        end: int = len(s)
        if end == 0:
            return True  #  empty string ε is always a valid subsequence of any string

        for char in t:
            if char == s[idx]:
                idx += 1
                if idx == end:
                    return True
        return False


def test_cases():
    cur_solution = Solution()
    inputs = (
        {"s": "abc", "t": "ahbgdc"},
        {"s": "axc", "t": "ahbgdc"},
    )
    outputs = [True, False]

    all_passed = True

    for i in range(len(inputs)):
        result = 0
        try:
            result = cur_solution.isSubsequence(**inputs[i])
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
