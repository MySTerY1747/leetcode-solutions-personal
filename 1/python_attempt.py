# You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.
#
# Given the string command, return the Goal Parser's interpretation of command.


class Solution(object):
    def twoSum(self, nums, target):
        hashed_num = {index: number for index, number in zip(range(len(nums)), nums)}
        hashed_num_backwards = {
            number: index for index, number in zip(range(len(nums)), nums)
        }
        for index in hashed_num:
            desired_number = target - hashed_num[index]
            if desired_number in hashed_num_backwards:
                if index != hashed_num_backwards[desired_number]:
                    return [index, hashed_num_backwards[desired_number]]


def test_cases():
    cur_solution = Solution()
    try:
        assert cur_solution.twoSum([3, 4, 5, 6], 7) == [0, 1]
        assert cur_solution.twoSum([4, 5, 6], 10) == [0, 2]
    except Exception as e:
        print(f"Test unsuccessful: {e=}")
    else:
        print("All test cases passed.")


if __name__ == "__main__":
    test_cases()
    cur_solution = Solution()
