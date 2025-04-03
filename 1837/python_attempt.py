# Given an integer n (in base 10) and a base k, return the sum of the digits of n after converting n from base 10 to base k.
#
# After converting, each digit should be interpreted as a base 10 number, and the sum should be returned in base 10.


class Solution(object):
    def sumBase(self, n, k):
        converted_n = ""
        while n > 0:
            dig = int(n % k)
            if dig < 10:
                converted_n += str(dig)
            else:
                converted_n += chr(ord("A") + dig - 10)  # Using uppercase letters
            n //= k
        converted_n = converted_n[::-1]

        return sum([int(number) for number in converted_n])


def test_cases():
    cur_solution = Solution()
    try:
        assert cur_solution.sumBase(34, 6) == 9
        assert cur_solution.sumBase(10, 10) == 1
    except Exception as e:
        print(f"Test unsuccessful: {e=}")
    else:
        print("All test cases passed.")


if __name__ == "__main__":
    test_cases()
