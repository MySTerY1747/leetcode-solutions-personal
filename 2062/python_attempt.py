# A substring is a contiguous (non-empty) sequence of characters within a string.
#
# A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it.
#
# Given a string word, return the number of vowel substrings in word.


class Solution(object):
    def countVowelSubstrings(self, word):
        total_count = 0
        cur_substring = set()
        vowels = "aeiou"
        for i, letter in enumerate(word):
            if letter in vowels:
                cur_substring.add(letter)
                for subletter in word[i:]:
                    if subletter in vowels:
                        cur_substring.add(subletter)
                    else:
                        break

                    if len(cur_substring) == 5:
                        total_count += 1
            cur_substring = set()
        return total_count


def test_cases():
    try:
        cur_solution = Solution()
        assert cur_solution.countVowelSubstrings("aeiouu") == 2
        assert cur_solution.countVowelSubstrings("unicornarihan") == 0
        assert cur_solution.countVowelSubstrings("cuaieuouac") == 7
    except Exception as e:
        print(f"Something went wrong: {e}")
    else:
        print("All test cases passed successfully.")


if __name__ == "__main__":
    test_cases()
    cur_solution = Solution()
    print(cur_solution.countVowelSubstrings("cuaieuouac"))
