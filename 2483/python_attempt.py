# You are given the customer visit log of a shop represented by a 0-indexed string customers consisting only of characters 'N' and 'Y':
#
#     if the ith character is 'Y', it means that customers come at the ith hour
#     whereas 'N' indicates that no customers come at the ith hour.
#
# If the shop closes at the jth hour (0 <= j <= n), the penalty is calculated as follows:
#
#     For every hour when the shop is open and no customers come, the penalty increases by 1.
#     For every hour when the shop is closed and customers come, the penalty increases by 1.
#
# Return the earliest hour at which the shop must be closed to incur a minimum penalty.
#
# Note that if a shop closes at the jth hour, it means the shop is closed at the hour j.


class Solution(object):
    def bestClosingTime(self, customers: str) -> int:
        best_hour: int = 0
        min_penalty: int = customers.count("Y")
        total_N_so_far: int = 0
        total_Y_left: int = min_penalty
        for hour, value in enumerate(customers):
            if value == "Y":
                #  calculate penalty, compare to min
                total_Y_left -= 1
                cur_penalty = total_N_so_far + total_Y_left
                if cur_penalty < min_penalty:
                    best_hour = hour + 1
                    min_penalty = cur_penalty
            else:
                total_N_so_far += 1
        return best_hour


def test_cases():
    cur_solution = Solution()
    inputs = (
        {"customers": "YYNY"},
        {"customers": "NNNNN"},
        {"customers": "YYYY"},
    )
    outputs = [2, 0, 4]

    all_passed = True

    for i in range(len(inputs)):
        result = 0
        try:
            result = cur_solution.bestClosingTime(**inputs[i])
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
