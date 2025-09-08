# Given the head of a linked list, remove the nth node from the end of the list and return its head.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        guide: ListNode | None = head
        real: ListNode | None = head
        #  1. Move guide ahead by n
        for _ in range(n):
            guide = guide.next

        #  2. Move both pointers together until guide hits None
        prev: ListNode | None = None
        while guide:
            prev = real
            real = real.next
            guide = guide.next

        #  3. Skip over node to remove
        if real == head:
            return real.next
        elif real.next:
            prev.next = real.next
        elif real.next is None and prev is not None:
            prev.next = None
        else:
            return None

        return head


if __name__ == "__main__":
    cur_solution = Solution()
    list_input = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    print("[1,2,3,4,5]")
    cur_solution.removeNthFromEnd(list_input, 2)
    print("Here's the outputted list: ")
    node = list_input
    while node:
        print(node.val)
        node = node.next
