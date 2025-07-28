# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# Implement the MinStack class:
#
#     MinStack() initializes the stack object.
#     void push(int val) pushes the element val onto the stack.
#     void pop() removes the element on the top of the stack.
#     int top() gets the top element of the stack.
#     int getMin() retrieves the minimum element in the stack.
#
# You must implement a solution with O(1) time complexity for each function.


class MinStack(object):
    def __init__(self):
        self.stackOne = []
        self.stackTwo = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stackOne.append(val)
        if not self.stackTwo or self.stackTwo[-1] >= val:
            self.stackTwo.append(val)

    def pop(self):
        """
        :rtype: None
        """
        if not self.stackOne:
            return None
        val = self.stackOne.pop()
        if self.stackTwo and self.stackTwo[-1] == val:
            self.stackTwo.pop()
        return val

    def top(self):
        """
        :rtype: int
        """
        return self.stackOne[-1] if self.stackOne else None

    def getMin(self):
        """
        :rtype: int
        """
        if self.stackTwo:
            return self.stackTwo[-1]
        return self.stackOne[-1] if self.stackOne else None
