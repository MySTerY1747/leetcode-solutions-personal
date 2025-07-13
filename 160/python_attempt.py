# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
#
# For example, the following two linked lists begin to intersect at node c1:
#
# The test cases are generated such that there are no cycles anywhere in the entire linked structure.
#
# Note that the linked lists must retain their original structure after the function returns.


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if headA == headB:
            return headA
        #  traverse headA list, keeping each node in a set
        #  traverse headB list, return first elm present in set
        node_set = set()
        cur_node = headA
        while cur_node is not None:
            node_set.add(cur_node)
            cur_node = cur_node.next

        cur_node = headB
        while cur_node is not None:
            if cur_node in node_set:
                return cur_node.val
            cur_node = cur_node.next
        return None


def test_cases():
    cur_solution = Solution()
    try:
        assert (
            cur_solution.getIntersectionNode([4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5]) == 2
        )
    except Exception as e:
        print(f"Test unsuccessful: {e=}")
    else:
        print("All test cases passed.")


if __name__ == "__main__":
    test_cases()
