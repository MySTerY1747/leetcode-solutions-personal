#  Given an array of strings strs, group the anagrams together. You can return the answer in any order.


class Solution(object):
    def groupAnagrams(self, strs):
        sorted_strs = {string: "".join(sorted(string)) for string in strs}
        anagrams = []
        existing_anagrams = {}
        for string in strs:
            if sorted_strs[string] in existing_anagrams:
                anagrams[existing_anagrams[sorted_strs[string]]].append(string)
            else:
                anagrams.append([string])
                existing_anagrams[sorted_strs[string]] = len(anagrams) - 1
        return anagrams


def test_cases():
    cur_solution = Solution()
    try:
        assert cur_solution.groupAnagrams(
            ["eat", "tea", "tan", "ate", "nat", "bat"]
        ) == [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        assert cur_solution.groupAnagrams(["a"]) == [["a"]]
    except Exception as e:
        print(f"Test unsuccessful: {e=}")
    else:
        print("All test cases passed.")


if __name__ == "__main__":
    test_cases()
    cur_solution = Solution()
    print(cur_solution.groupAnagrams(["", ""]))
