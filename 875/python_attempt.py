# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
#
# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
#
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
#
# Return the minimum integer k such that she can eat all the bananas within h hours.

from math import ceil


class Solution(object):
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        minimum: int = max(sum(piles) // h, 1)
        maximum: int = max(piles)

        while minimum != maximum:
            cur_hours: int = 0
            mid: int = (minimum + maximum) // 2
            for elm in piles:
                cur_hours += ceil(elm / mid)
            if cur_hours > h:
                minimum = mid + 1
            elif cur_hours <= h:
                maximum = mid

        return minimum


def test_cases():
    cur_solution = Solution()
    inputs = (
        {"piles": [3, 6, 7, 11], "h": 8},
        {"piles": [30, 11, 23, 4, 20], "h": 5},
        {"piles": [30, 11, 23, 4, 20], "h": 6},
    )
    outputs = [4, 30, 23]

    all_passed = True

    for i in range(len(inputs)):
        result = 0
        try:
            result = cur_solution.minEatingSpeed(**inputs[i])
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
