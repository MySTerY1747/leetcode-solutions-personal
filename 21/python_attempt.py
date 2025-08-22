# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
#
# Return the head of the merged linked list.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:
        #  INFO: First attempt
        #
        # new_list = ListNode()  #  dummy node
        # first_node = new_list
        # #  going to use the same approach as the merge algorithm in merge-sort
        # while (list1 is not None) and (list2 is not None):
        #     if list1.val > list2.val:
        #         new_list.next = ListNode(val=list2.val)
        #         new_list = new_list.next
        #         list2 = list2.next
        #     else:
        #         new_list.next = ListNode(val=list1.val)
        #         list1 = list1.next
        #         new_list = new_list.next
        # non_empty_list = list1 if list2 is None else list2
        # while non_empty_list is not None:
        #     new_list.next = ListNode(val=non_empty_list.val)
        #     non_empty_list = non_empty_list.next
        #     new_list = new_list.next
        # return first_node.next
        #
        #  INFO: Second attempt

        # SENTINEL: int = 500  #  max value in def is 100
        #
        # list1 = ListNode(val=SENTINEL) if list1 is None else list1
        # list2 = ListNode(val=SENTINEL) if list2 is None else list2
        #
        # node: ListNode = ListNode()
        # first_node: ListNode = node
        #
        # while (list1.val != SENTINEL) or (list2.val != SENTINEL):
        #     if list1.val <= list2.val:
        #         node.next = ListNode(list1.val)
        #         list1 = list1.next
        #         list1 = ListNode(val=SENTINEL) if list1 is None else list1
        #     else:
        #         node.next = ListNode(list2.val)
        #         list2 = list2.next
        #         list2 = ListNode(val=SENTINEL) if list2 is None else list2
        #     node = node.next
        #
        # return first_node.next

        #  INFO: Third attempt

        node: ListNode = ListNode()
        first_node: ListNode = node

        while list1 and list2:
            if list1.val <= list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        if list1:
            node.next = list1
        else:
            node.next = list2

        return first_node.next


if __name__ == "__main__":
    pass
