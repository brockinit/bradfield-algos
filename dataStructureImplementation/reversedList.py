class Stack(object):

    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def size(self):
        return len(self._items)

'''
    Using the stack implementation above, write a function
    that returns a reversed copy of a list.

    To achieve this, the a new stack is created and has the items added to it. Once added,
    the items are popped from the stack and added back to the list, effectively reversing the order
    of all items in the list.
'''
def reverseList(alist):
    stack = Stack()
    newlist = []
    for item in alist:
        stack.push(item)
    while not stack.is_empty():
        newlist.append(stack.pop())
    return newlist


assert reverseList([1, 2, 3]) == [3, 2, 1], "list not reversed!"
assert reverseList([2, 2, 3]) == [3, 2, 2], "list not reversed!"
assert reverseList([2, 2, 3, 5, 7, 8]) == [8, 7, 5, 3, 2, 2], "list not reversed!"

