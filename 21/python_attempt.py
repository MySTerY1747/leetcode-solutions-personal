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
    def mergeTwoLists(self, list1, list2):
        new_list = ListNode()  #  dummy node
        first_node = new_list
        #  going to use the same approach as the merge algorithm in merge-sort
        while (list1 is not None) and (list2 is not None):
            if list1.val > list2.val:
                new_list.next = ListNode(val=list2.val)
                new_list = new_list.next
                list2 = list2.next
            else:
                new_list.next = ListNode(val=list1.val)
                list1 = list1.next
                new_list = new_list.next
        while list1 is not None:
            new_list.next = ListNode(val=list1.val)
            list1 = list1.next
            new_list = new_list.next
        while list2 is not None:
            new_list.next = ListNode(val=list2.val)
            list2 = list2.next
            new_list = new_list.next
        return first_node.next


if __name__ == "__main__":
    pass
