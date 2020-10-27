class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        #return self.items == []
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        #last = len(self.items) - 1
        #return self.items[last]
        return self.items[-1]

    def size(self):
        return len(self.items)


# 文字列を逆順にする
stack = Stack()
for c in "Hello":
    stack.push(c)

reverse = ""

while stack.size():
    reverse += stack.pop()

print(reverse)
