# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


class Solution(object):
    def maxProfit(self, prices: list[int]) -> int:
        #  INFO: My first version:
        # max_profit: int = 0
        # right_min: int = 10001  #  over limit according to spec
        # right_max: int = 0
        # for elm in prices[::-1]:
        #     if elm < right_min:
        #         right_min = elm
        #         if (right_max - right_min) > max_profit:
        #             max_profit = right_max - right_min
        #     if elm > right_max:
        #         right_max = elm
        #         right_min = elm
        #
        # return max_profit

        #  INFO: Second (far simpler) version
        max_profit: int = 0
        price_min: int = 10001  #  over limit
        for price in prices:
            if price_min > price:
                price_min = price
            if max_profit < (price - price_min):
                max_profit = price - price_min

        return max_profit


def test_cases():
    cur_solution = Solution()
    inputs = (
        {"prices": [7, 1, 5, 3, 6, 4]},
        {"prices": [7, 6, 4, 3, 1]},
        {"prices": [2, 4, 1]},
    )
    outputs = [5, 0, 2]

    all_passed = True

    for i in range(len(inputs)):
        result = 0
        try:
            result = cur_solution.maxProfit(**inputs[i])
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
