class Node:
    def __init__(self, task):
        self.task = task
        self.next = None  

class ToDoList:
    def __init__(self):
        self.head = None  

    def append(self, task):
        new_node = Node(task)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node  

    def display(self):
        temp = self.head
        while temp:
            print(temp.task, end=" -> ")
            temp = temp.next
        print("None")  

todo = ToDoList()
todo.append("Games") 
todo.append("Homework") 
todo.append("Sleep")
todo.display()
