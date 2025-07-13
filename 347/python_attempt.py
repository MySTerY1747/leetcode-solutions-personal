# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


class Solution(object):
    def topKFrequent(self, nums, k):
        #  traverse list, make hash map of count per element
        #  pop elm with highest count, add to return list
        count_dict = {}
        output_list = []
        for elm in nums:
            count_dict[elm] = count_dict.get(elm, 0) + 1
        for _ in range(k):
            max_elm = max(count_dict, key=count_dict.get)
            count_dict.pop(max_elm)
            output_list.append(max_elm)
        return output_list


def test_cases():
    cur_solution = Solution()
    try:
        assert cur_solution.topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
        assert cur_solution.topKFrequent([1], 1) == 1
    except Exception as e:
        print(f"Test unsuccessful: {e=}")
    else:
        print("All test cases passed.")


if __name__ == "__main__":
    test_cases()
