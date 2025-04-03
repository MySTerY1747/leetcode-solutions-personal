# Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.
#
# A subarray is a contiguous subsequence of the array.


class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        cur_total = 0
        # for i in range(len(arr)):
        #     print(f"{arr[i]=}")
        #     cur_total += arr[i]
        # for i in range(len(arr) - 2):
        #     print(f"{arr[i:i+3]=}")
        #     cur_total += sum(arr[i : i + 3])
        # for i in range(len(arr) - 4):
        #     print(f"{arr[i:i+5]=}")
        #     cur_total += sum(arr[i : i + 5])
        for odd_number in range(1, len(arr) + 1, 2):
            for i in range(len(arr) - odd_number + 1):
                cur_total += sum(arr[i : i + odd_number])
        return cur_total


def test_cases():
    cur_solution = Solution()
    try:
        assert cur_solution.sumOddLengthSubarrays([1, 4, 2, 5, 3]) == 58
        assert cur_solution.sumOddLengthSubarrays([1, 2]) == 3
        assert cur_solution.sumOddLengthSubarrays([10, 11, 12]) == 66
    except Exception as e:
        print(f"Test unsuccessful: {e=}")
    else:
        print("All test cases passed.")


if __name__ == "__main__":
    test_cases()
    cur_solution = Solution()
    # print(cur_solution.sumOddLengthSubarrays([1, 4, 2, 5, 3]))
