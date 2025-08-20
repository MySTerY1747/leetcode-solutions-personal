# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.
#
# Implement the TimeMap class:
#
#     TimeMap() Initializes the object of the data structure.
#     void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
#     String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".


class TimeMap:
    def __init__(self):
        self.key_dict: dict[str, dict] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_dict.keys():
            self.key_dict[key] = {"timestamps": [timestamp]}
        else:
            self.key_dict[key]["timestamps"].append(timestamp)

        self.key_dict[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_dict.keys():
            return ""

        nums = self.key_dict[key]["timestamps"]
        target = timestamp
        result = -1

        left: int = 0
        right: int = len(nums) - 1

        while left <= right:
            mid: int = (left + right) // 2
            if left == right:
                result = nums[left] if target >= nums[left] else -1
                break
            elif nums[mid] <= target < nums[mid + 1]:
                result = nums[mid]
                break
            elif target == nums[mid + 1]:
                result = target
                break
            elif nums[mid] > target:
                right: int = mid - 1
            else:
                left: int = mid + 1
        else:
            result = -1

        return "" if result == -1 else self.key_dict[key][result]


# def test_cases():
#     cur_solution = Solution()
#     inputs = ()
#     outputs = []
#
#     all_passed = True
#
#     for i in range(len(inputs)):
#         result = 0
#         try:
#             result = cur_solution.search(**inputs[i])
#             assert result == outputs[i]
#         except AssertionError:
#             all_passed = False
#             input_str = ", ".join(
#                 [f"{key}={value}" for key, value in inputs[i].items()]
#             )
#             print(
#                 f"• 🟥 Test {i + 1} failed: Input: {input_str}. Expected: {outputs[i]}, Got: {result}\n"
#             )
#         except Exception as e:
#             all_passed = False
#             print(f"❗️Unexpected error on test {i + 1}: {e}")
#
#     if all_passed:
#         print("✅ All test cases passed!")
#
#
# if __name__ == "__main__":
#     test_cases()
