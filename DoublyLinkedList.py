class Node:
    def __init__(self, info):
        self.info = info
        self.next_link = None
        self.prev_link = None

class DoublyLinkedList:
    def __init__(self):
        self.start = None
        self.end = None

    def append(self, info):
        new_node = Node(info)
        if not self.start:
            self.start = new_node
            self.end = new_node
            return
        self.end.next_link = new_node
        new_node.prev_link = self.end
        self.end = new_node

    def display(self):
        temp = self.start
        while temp:
            print(temp.info, end=" <-> ")
            temp = temp.next_link
        print("None")

print("\nBrowser History (Doubly Linked List):")
browser_history = DoublyLinkedList()
browser_history.append("Google")
browser_history.append("Wikipedia")
browser_history.append("GitHub")
browser_history.display()
