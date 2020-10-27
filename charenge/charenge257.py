class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


# 文字列を逆順にする
stack = Stack()
for c in "yesterday":
    stack.push(c)

reverse = ""

while stack.size():
    reverse += stack.pop()

print(reverse)


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

a_queue = Queue()
normal_list = [0,1,2,3,4]

for i in normal_list:
    a_queue.enqueue(i)

print(normal_list)
print(a_queue.items)
