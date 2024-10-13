from typing import Any

'''
class Stack:
    def __init__(self) -> None:
        self.stack = []

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def push(self, item) -> None:
        self.stack.append(item)

    def pop(self) -> Any:
        if not self.is_empty():
            return self.stack.pop()
        print('Stack is empty')

    def peek(self) -> Any:
        if not self.is_empty():
            return self.stack[-1]
        print('Stack is empty')

    def size(self) -> int:
        return len(self.stack)


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)

stack.pop()
stack.pop()

print(stack.peek())

'''


class Queue:
    def __init__(self) -> None:
        self.queue = []

    def is_empty(self) -> bool:
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def peek(self):
        if not self.is_empty():
            return self.queue[0]

    def enqueue(self, item) -> None:
        self.queue.append(item)

    def dequeue(self) -> Any:
        if not self.is_empty():
            self.queue.pop(0)

queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)

queue.dequeue()
queue.dequeue()
print(queue.peek())
