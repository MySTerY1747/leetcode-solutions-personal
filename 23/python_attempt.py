# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
#
# Merge all the linked-lists into one sorted linked-list and return it.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if (not lists) or (len(lists) == 1 and lists[0] == []):
            return None

        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeTwoLists(list1, list2))
            lists = mergedLists
        return lists[0]

    def mergeTwoLists(
        self, list1: list[ListNode | None], list2: list[ListNode | None]
    ) -> list[ListNode | None]:
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
