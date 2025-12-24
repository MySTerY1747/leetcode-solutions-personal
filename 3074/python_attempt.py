# You are given an array apple of size n and an array capacity of size m.
#
# There are n packs where the ith pack contains apple[i] apples. There are m boxes as well, and the ith box has a capacity of capacity[i] apples.
#
# Return the minimum number of boxes you need to select to redistribute these n packs of apples into boxes.
#
# Note that, apples from the same pack can be distributed into different boxes.


class Solution(object):
    def minimumBoxes(self, apple: list[int], capacity: list[int]) -> int:
        apples = sum(apple)
        capacity.sort()
        idx: int = len(capacity) - 1
        boxes: int = 0
        while apples > 0:
            apples -= capacity[idx]
            idx -= 1
            boxes += 1
        return boxes


def test_cases():
    cur_solution = Solution()
    inputs = (
        {"apple": [1, 3, 2], "capacity": [4, 3, 1, 5, 2]},
        {"apple": [5, 5, 5], "capacity": [2, 4, 2, 7]},
    )
    outputs = [2, 4]

    all_passed = True

    for i in range(len(inputs)):
        result = 0
        try:
            result = cur_solution.minimumBoxes(**inputs[i])
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
