class Node:
    def __init__(self, info):
        self.info = info
        self.link = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, info):
        new_node = Node(info)
        new_node.link = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            return None
        removed_data = self.top.info
        self.top = self.top.link
        return removed_data

    def display(self):
        temp = self.top
        while temp:
            print(temp.info, end=' -> ')
            temp = temp.link
        print('None')

print("\nUndo/Redo (Stack):")
stack = Stack()
stack.push("Action 1")
stack.push("Action 2")
stack.push("Action 3")
stack.display()
print("Popped:", stack.pop())
stack.display()
