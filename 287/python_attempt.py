# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
#
# There is only one repeated number in nums, return this repeated number.
#
# You must solve the problem without modifying the array nums and using only constant extra space.


class Solution(object):
    def findDuplicate(self, nums: list[int]) -> int:
        #   I hate this problem more than words can describe
        #   The answer relies entirely on memorization, it's not a problem that you can (realistically) just sit down and power your way through
        slow_pointer: int = 0
        fast_pointer: int = 0
        intersected: bool = False
        while not intersected:
            slow_pointer = nums[slow_pointer]
            fast_pointer = nums[nums[fast_pointer]]
            if slow_pointer == fast_pointer:
                intersected = True

        second_slow_pointer: int = 0
        while True:
            slow_pointer = nums[slow_pointer]
            second_slow_pointer = nums[second_slow_pointer]
            if slow_pointer == second_slow_pointer:
                return slow_pointer


def test_cases():
    cur_solution = Solution()
    inputs = (
        {"nums": [1, 3, 4, 2, 2]},
        {"nums": [3, 1, 3, 4, 2]},
        {"nums": [3, 3, 3, 3, 3]},
    )
    outputs = [2, 3, 3]

    all_passed = True

    for i in range(len(inputs)):
        result = 0
        try:
            result = cur_solution.findDuplicate(**inputs[i])
            assert result == outputs[i]
        except AssertionError:
            all_passed = False
            input_str = ", ".join(
                [f"{key}={value}" for key, value in inputs[i].items()]
            )
            print(
                f"• 🟥 Test {i + 1} failed: Input: {input_str}. Expected: {outputs[i]}, Got: {result}\n"
            )
        except Exception as e:
            all_passed = False
            print(f"❗️Unexpected error on test {i + 1}: {e}")

    if all_passed:
        print("✅ All test cases passed!")


if __name__ == "__main__":
    test_cases()
