class Stack:

    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

    def push(self, item):
        self._items.insert(0, item)

    def pop(self):
        return self._items.pop(0)

    def peek(self):
        return self._items[0]

    def size(self):
        return len(self._items)

class Queue:
    def __init__(self):
        self._s1 = Stack()
        self._s2 = Stack()

    def is_empty(self):
        return self._s1.is_empty() and self._s2.is_empty()

    def size(self):
        return self._s1.size() + self._s2.size()

    def enqueue(self, item):
        self._s1.push(item)

    def dequeue(self, item):
        if self._s2.is_empty():
            while not self._s1.is_empty():
                self._s2.push(self._s1.pop())
        return self._s2.pop()


