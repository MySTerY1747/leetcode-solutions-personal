# Given head, the head of a linked list, determine if the linked list has a cycle in it.
#
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
#
# Return true if there is a cycle in the linked list. Otherwise, return false.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head: ListNode | None) -> bool:
        #  INFO:  For some reason, removing the
        #  type indicators SIGNIFICANTLY speeds up the code on Leetcode...
        node_set: set[ListNode] = set()

        node: ListNode | None = head
        while node is not None:
            if node in node_set:
                return True
            else:
                node_set.add(node)
                node = node.next
        return False


if __name__ == "__main__":
    pass
