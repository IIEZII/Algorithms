class Node:
    def __init__(self, info):
        self.info = info
        self.link = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, info):
        new_node = Node(info)
        if not self.rear:
            self.front = self.rear = new_node
            return
        self.rear.link = new_node
        self.rear = new_node

    def dequeue(self):
        if not self.front:
            return None
        removed_data = self.front.info
        self.front = self.front.link
        if not self.front:
            self.rear = None
        return removed_data

    def display(self):
        temp = self.front
        while temp:
            print(temp.info, end=' <- ')
            temp = temp.link
        print('None')

print("\nCustomer Service (Queue):")
queue = Queue()
queue.enqueue("Customer 1")
queue.enqueue("Customer 2")
queue.enqueue("Customer 3")
queue.display()
print("Dequeued:", queue.dequeue())
queue.display()
 # type: ignore