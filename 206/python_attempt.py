# Given the head of a singly linked list, reverse the list, and return the reversed list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev: ListNode | None = None

        while head is not None:
            nextNode: ListNode | None = head.next
            head.next = prev
            prev = head
            head = nextNode
        return prev


def test_cases():
    cur_solution = Solution()
    inputs = (
        {"head": ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))},
        {"head": ListNode(1, ListNode(2))},
    )
    outputs = [
        ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1))))),
        ListNode(2, ListNode(1)),
    ]

    all_passed = True

    for i in range(len(inputs)):
        result = 0
        try:
            result = cur_solution.reverseList(**inputs[i])
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
