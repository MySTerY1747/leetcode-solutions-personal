# You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.
#
# Given the string command, return the Goal Parser's interpretation of command.


class Solution(object):
    def interpret(self, command):
        parser_dict = {"G": "G", "()": "o", "(al)": "al"}
        split_command = []
        cur_word = ""
        for i, letter in enumerate(command):
            if letter in parser_dict:
                split_command.append(letter)
            else:
                cur_word += letter
            if cur_word in parser_dict:
                split_command.append(cur_word)
                cur_word = ""
        return "".join([parser_dict[elm] for elm in split_command])


def test_cases():
    cur_solution = Solution()
    try:
        assert cur_solution.interpret("G()(al)") == "Goal"
        assert cur_solution.interpret("G()()()()(al)") == "Gooooal"
        assert cur_solution.interpret("(al)G(al)()()G") == "alGalooG"
    except Exception as e:
        print(f"Test unsuccessful: {e=}")
    else:
        print("All test cases passed.")


if __name__ == "__main__":
    test_cases()
    cur_solution = Solution()
    # print(cur_solution.sumOddLengthSubarrays([1, 4, 2, 5, 3]))
