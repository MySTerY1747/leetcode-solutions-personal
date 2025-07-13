from leetcode_tester import LeetCodeTester

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
    tester = LeetCodeTester(49)
    # Add test cases
    tester.add_test_case(
        method_name="groupAnagrams",
        args=[["eat", "tea", "tan", "ate", "nat", "bat"]],
        expected_output=[["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        description="Example 1 from problem description",
    )

    tester.add_test_case(
        method_name="groupAnagrams",
        args=[[""]],
        expected_output=[[""]],
        description="Example 2 - Empty string",
    )

    tester.add_test_case(
        method_name="groupAnagrams",
        args=[["a"]],
        expected_output=[["a"]],
        description="Example 3 - Single character",
    )

    tester.add_test_case(
        method_name="groupAnagrams",
        args=[["", ""]],
        expected_output=[["", ""]],
        description="Multiple empty strings",
    )

    tester.add_test_case(
        method_name="groupAnagrams",
        args=[["abc", "cba", "bac", "foo", "oof"]],
        expected_output=[["abc", "cba", "bac"], ["foo", "oof"]],
        description="Multiple anagram groups",
    )

    # Run tests
    tester.run_tests()
