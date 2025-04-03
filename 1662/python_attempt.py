# Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
#
# A string is represented by an array if the array elements concatenated in order forms the string.


class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        return "".join(word1) == "".join(word2)


def test_cases():
    cur_solution = Solution()
    try:
        assert (
            cur_solution.arrayStringsAreEqual(word1=["ab", "c"], word2=["a", "bc"])
            is True
        )
        assert (
            cur_solution.arrayStringsAreEqual(word1=["a", "cb"], word2=["ab", "c"])
            is False
        )
        assert (
            cur_solution.arrayStringsAreEqual(
                word1=["abc", "d", "defg"], word2=["abcddefg"]
            )
            is True
        )
    except Exception as e:
        print(f"Test unsuccessful: {e=}")
    else:
        print("All test cases passed.")


if __name__ == "__main__":
    test_cases()
    cur_solution = Solution()
    print(cur_solution.arrayStringsAreEqual([3, 5]))
