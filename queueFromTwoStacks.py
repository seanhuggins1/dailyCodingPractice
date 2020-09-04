#
# Script implements a queue using two stacks
#
class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if self.size() == 0: return None
        return self.items.pop()
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)

class TwoStackQueue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
    def enqueue(self, elem):
        self.s1.push(elem)
    def dequeue(self):
        if self.s2.isEmpty():
            while not self.s1.isEmpty():
                self.s2.push(self.s1.pop())
        return self.s2.pop()

stack = Stack()
stack.push(5)
stack.push(10)
stack.push(15)
print(stack.pop())
print(stack.pop())
print(stack.pop())

queue = TwoStackQueue()
print(queue.dequeue())




