# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
#
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
#
# You may not alter the values in the list's nodes, only nodes themselves may be changed.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        if k == 1:
            return head

        start_node: ListNode | None = head
        first_iteration: bool = True
        previous_group_end: ListNode | None = None
        while True:
            if start_node:
                local_start: ListNode = start_node
                cur_node: ListNode = local_start
                nodes_added: int = 1
                prev: ListNode | None = None
                final_next: ListNode | None = None
                temp = cur_node
                count = 0
                for _ in range(k):
                    if not temp:
                        break
                    temp = temp.next
                    count += 1
                if count < k:
                    break
                final_next = temp

                for _ in range(k - 1):
                    if cur_node.next:
                        next_node: ListNode = cur_node.next
                        cur_node.next = prev
                        prev = cur_node
                        cur_node = next_node
                        nodes_added += 1
                    else:
                        break
                cur_node.next = prev
                if first_iteration:
                    head = cur_node
                    first_iteration = False
                else:
                    previous_group_end.next = cur_node
                local_start.next = final_next
                previous_group_end = local_start
                start_node = local_start.next
                if nodes_added != k:
                    break
            else:
                break
        return head
