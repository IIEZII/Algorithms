class Node:
    def __init__(self, info):
        self.info = info
        self.link = None

class SinglyLinkedList:
    def __init__(self):
        self.start = None

    def append(self, info):
        new_node = Node(info)
        if not self.start:
            self.start = new_node
            return
        last = self.start
        while last.link:
            last = last.link
        last.link = new_node

    def prepend(self, info):
        new_node = Node(info)
        new_node.link = self.start
        self.start = new_node

    def remove(self, info):
        temp = self.start
        if temp and temp.info == info:
            self.start = temp.link
            return
        prev = None
        while temp and temp.info != info:
            prev = temp
            temp = temp.link
        if temp:
            prev.link = temp.link

    def display(self):
        temp = self.start
        while temp:
            print(temp.info, end=' -> ')
            temp = temp.link
        print('None')

if __name__ == "__main__":
    todo_list = SinglyLinkedList()
    
    while True:
        print("\n[1] Append Task")
        print("[2] Prepend Task")
        print("[3] Remove Task")
        print("[4] Display List")
        print("[5] Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            task = input("Enter task to append: ")
            todo_list.append(task)
        elif choice == '2':
            task = input("Enter task to prepend: ")
            todo_list.prepend(task)
        elif choice == '3':
            task = input("Enter task to remove: ")
            todo_list.remove(task)
        elif choice == '4':
            todo_list.display()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.")
