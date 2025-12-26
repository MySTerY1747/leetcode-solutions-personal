# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        #  pure math version
        #  part 1: decoding the numbers and summing them

        # l2_num: int = 0  #  defined as non-negative, so this is safe
        # l1_num: int = 0  #  defined as non-negative, so this is safe
        #
        # cur_l1: ListNode | None = l1
        # index: int = 0
        # while cur_l1:
        #     l1_num += cur_l1.val * 10**index
        #     cur_l1 = cur_l1.next
        #     index += 1
        #
        # cur_l2: ListNode | None = l2
        # index: int = 0
        # while cur_l2:
        #     l2_num += cur_l2.val * 10**index
        #     cur_l2 = cur_l2.next
        #     index += 1
        #
        # total_sum: int = l1_num + l2_num
        #
        # #  part 2: writing the new number
        #
        # new_head = ListNode(total_sum % 10)
        # cur_node = new_head
        # index: int = 2
        # while (total_sum // 10 ** (index - 1)) != 0:
        #     cur_node.next = ListNode((total_sum % 10**index) // 10 ** (index - 1))
        #     cur_node = cur_node.next
        #     index += 1
        #
        # return new_head

        #  hybrid version that gets the best runtime
        l1_num: int = 0  #  defined as non-negative, so this is safe
        l2_num: int = 0  #  defined as non-negative, so this is safe

        cur_l1: ListNode | None = l1
        index: int = 0
        while cur_l1:
            l1_num += cur_l1.val * 10**index
            cur_l1 = cur_l1.next
            index += 1

        cur_l2: ListNode | None = l2
        index: int = 0
        while cur_l2:
            l2_num += cur_l2.val * 10**index
            cur_l2 = cur_l2.next
            index += 1

        total_sum: int = l1_num + l2_num

        #  part 2: writing the new number

        sum_reversed: str = str(total_sum)[::-1]
        new_head = ListNode(int(sum_reversed[0])) if sum_reversed else None
        cur_node = new_head
        for num in sum_reversed[1::]:
            cur_node.next = ListNode(int(num))
            cur_node = cur_node.next

        return new_head
