class Node:
    def __init__(self, info):
        self.info = info
        self.next_link = None

class CircularLinkedList:
    def __init__(self):
        self.start = None

    def append(self, info):
        new_node = Node(info)
        if not self.start:
            self.start = new_node
            new_node.next_link = self.start
            return
        temp = self.start
        while temp.next_link != self.start:
            temp = temp.next_link
        temp.next_link = new_node
        new_node.next_link = self.start

    def display(self):
        temp = self.start
        if not temp:
            return
        while True:
            print(temp.info, end=" -> ")
            temp = temp.next_link
            if temp == self.start:
                break
        print("(back to start)")

print("\nTask Rotation (Circular Linked List):")
task_scheduler = CircularLinkedList()
task_scheduler.append("Task 1")
task_scheduler.append("Task 2")
task_scheduler.append("Task 3")
task_scheduler.display()
