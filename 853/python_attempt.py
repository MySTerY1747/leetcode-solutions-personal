# There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.
#
# You are given two integer arrays position and speed, both of length n, where position[i] is the starting mile of the ith car and speed[i] is the speed of the ith car in miles per hour.
#
# A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.
#
# A car fleet is a car or cars driving next to each other. The speed of the car fleet is the minimum speed of any car in the fleet.
#
# If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.
#
# Return the number of car fleets that will arrive at the destination.


class Solution(object):
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        stack: list[float] = []
        position_speed = {pos: cur_speed for pos, cur_speed in zip(position, speed)}
        position.sort(reverse=True)

        for cur_pos in position:
            finish_time: float = (target - cur_pos) / position_speed[cur_pos]
            if (not stack) or finish_time > stack[-1]:
                stack.append(finish_time)

        return len(stack)


def test_cases():
    cur_solution = Solution()
    inputs = (
        {"target": 12, "position": [10, 8, 0, 5, 3], "speed": [2, 4, 1, 1, 3]},
        {"target": 10, "position": [3], "speed": [3]},
        {"target": 100, "position": [0, 2, 4], "speed": [4, 2, 1]},
    )
    outputs = [3, 1, 1]

    all_passed = True

    for i in range(len(inputs)):
        result = 0
        try:
            result = cur_solution.carFleet(**inputs[i])
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
