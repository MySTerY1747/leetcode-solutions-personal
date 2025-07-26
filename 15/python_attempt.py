# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.


class Solution(object):
    def threeSum(self, nums):
        #  FIRST VERSION:
        # output_list = []
        # previous_tuples = set()
        # num_dict = {idx: num for idx, num in enumerate(nums)}
        # reversed_num_dict = {num: set() for num in nums}
        # for idx, num in enumerate(nums):
        #     reversed_num_dict[num].add(idx)
        #
        # for idx, num in enumerate(nums):
        #     target = 0 - num
        #     full_nums = set()
        #     for subidx in range(idx + 1, len(nums)):
        #         if nums[subidx] in full_nums:
        #             continue
        #         desired_num = target - num_dict[subidx]
        #         if desired_num in reversed_num_dict:
        #             if (
        #                 len(reversed_num_dict[desired_num].difference({idx, subidx}))
        #                 > 0
        #             ):
        #                 triplet_list = [num, num_dict[subidx], desired_num]
        #                 sorted_tuple = tuple(sorted(triplet_list))
        #                 if sorted_tuple not in previous_tuples:
        #                     output_list.append([num, num_dict[subidx], desired_num])
        #                     previous_tuples.add(sorted_tuple)
        #         full_nums.add(num_dict[subidx])
        # return output_list
        #  SECOND (BETTER) VERSION:
        nums.sort()
        output_array = []

        outer_index = 0
        while outer_index < len(nums):
            if outer_index != 0 and nums[outer_index - 1] == nums[outer_index]:
                outer_index += 1
                continue

            target = 0 - nums[outer_index]
            inner_min_index = outer_index + 1
            inner_max_index = len(nums) - 1
            while inner_min_index < inner_max_index:
                cur_sum = nums[inner_min_index] + nums[inner_max_index]
                if cur_sum == target:
                    cur_output_list = [
                        nums[outer_index],
                        nums[inner_min_index],
                        nums[inner_max_index],
                    ]
                    output_array.append(cur_output_list)
                    inner_min_index += 1
                    inner_max_index -= 1

                    while (
                        inner_min_index < inner_max_index
                        and nums[inner_min_index] == nums[inner_min_index - 1]
                    ):
                        inner_min_index += 1

                    while (
                        inner_min_index < inner_max_index
                        and nums[inner_max_index] == nums[inner_max_index + 1]
                    ):
                        inner_max_index -= 1

                elif cur_sum > target:
                    inner_max_index -= 1
                elif cur_sum < target:
                    inner_min_index += 1

            outer_index += 1
        return output_array


def test_cases():
    cur_solution = Solution()
    try:
        assert cur_solution.threeSum(nums=[-1, 0, 1, 2, -1, -4]) == [
            [-1, -1, 2],
            [-1, 0, 1],
        ]
        assert cur_solution.threeSum(nums=[0, 1, 1]) == []
        assert cur_solution.threeSum(nums=[0, 0, 0]) == [[0, 0, 0]]

    except Exception as e:
        print(f"Test unsuccessful: {e=}")
    else:
        print("All test cases passed.")


if __name__ == "__main__":
    test_cases()
