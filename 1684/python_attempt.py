# You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.
#
# Return the number of consistent strings in the array words.


class Solution(object):
    def countConsistentStrings(self, allowed, words):
        allowed_set = set(allowed)
        cur_total = 0
        for word in words:
            for character in word:
                if character not in allowed_set:
                    break
            else:
                cur_total += 1
        return cur_total


def test_cases():
    cur_solution = Solution()
    try:
        assert (
            cur_solution.countConsistentStrings(
                allowed="ab", words=["ad", "bd", "aaab", "baa", "badab"]
            )
            == 2
        )
        assert (
            cur_solution.countConsistentStrings(
                allowed="abc", words=["a", "b", "c", "ab", "ac", "bc", "abc"]
            )
            == 7
        )
        assert (
            cur_solution.countConsistentStrings(
                allowed="cad", words=["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]
            )
            == 4
        )
    except Exception as e:
        print(f"Test unsuccessful: {e=}")
    else:
        print("All test cases passed.")


if __name__ == "__main__":
    test_cases()
    cur_solution = Solution()
    print(cur_solution.countConsistentStrings([3, 5]))
