# You are given the head of a singly linked-list. The list can be represented as:
#
# L0 → L1 → … → Ln - 1 → Ln
#
# Reorder the list to be on the following form:
#
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
#
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reorderList(self, head: ListNode) -> None:
        #  1. Traverse list to find mid-point
        node: ListNode | None = head
        length: int = 0
        while node:
            length += 1
            node = node.next
        midpoint_index: int = length // 2

        #  2. Reverse latter half and cut off first half
        node = head
        prev: ListNode | None = None
        cur_index: int = 0
        while node:
            if cur_index >= midpoint_index:
                next_node: ListNode | None = node.next
                node.next = prev
                prev = node
                node = next_node
            elif cur_index == (midpoint_index - 1):  #  Cut off first list
                next_node = node.next
                node.next = None
                node = next_node
            else:
                node = node.next
            cur_index += 1
        second_half: ListNode | None = prev

        # 3. Merge lists
        first_half = head
        node = head
        first_half = first_half.next  # move past the head, since it's already in place

        while first_half or second_half:
            if second_half:
                temp = second_half.next
                node.next = second_half
                second_half.next = None
                node = node.next
                second_half = temp

            if first_half:
                temp = first_half.next
                node.next = first_half
                first_half.next = None
                node = node.next
                first_half = temp


if __name__ == "__main__":
    cur_solution = Solution()
    list_input = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    cur_solution.reorderList(list_input)
    print("Here's the outputted list: ")
    node = list_input
    while node:
        print(node.val)
        node = node.next
