class Solution(object):
    def kthDistinct(self, arr: list[str], k: int):
        filtered_list: list[str] = [elm for elm in arr if arr.count(elm) == 1]
        result: str = ""
        if len(filtered_list) >= k:
            result += filtered_list[k - 1]
        return result


def test_cases():
    cur_solution = Solution()
    try:
        assert cur_solution.kthDistinct(["d", "b", "c", "b", "c", "a"], 2) == "a"
    except Exception as e:
        print(f"Test unsuccessful: {e}")
    else:
        print("All test cases passed.")


if __name__ == "__main__":
    test_cases()
