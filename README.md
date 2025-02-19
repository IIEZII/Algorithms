## Linked List  
A **Linked List** is a linear data structure where each element (node) is connected to the next using pointers.

### **Singly Linked List**  
A **Singly Linked List** is a data structure where each node contains two parts, which are **Data** (the value stored in the node), 
and **Next pointer** (a reference to the next node in the sequence)  

It allows traversal **only in one direction** and does not have a link to the previous node.  
[View Code](https://github.com/IIEZII/Algorithms/blob/master/SinglyLinkedList.py) || [Asciinema Demo](https://asciinema.org/a/bZondSCLGm4PE4UUmX6zuRiUj)

### **Doubly Linked List**  
A **Doubly Linked List** is a type of linked list where each node contains: **Data**, **Next pointer** (points to the next node), and **Previous pointer** (points to the previous node)  

This allows **movement both forward and backward**, unlike a singly linked list.  
[View Code](https://github.com/IIEZII/Algorithms/blob/master/DoublyLinkedList.py) || [Asciinema Demo](https://asciinema.org/a/B0NHYj13v6oatOdbHAnjiS34u)

### **Circular Linked List**  
A **Circular Linked List** is a linked list where the last node points back to the first node, forming a **circular connection**.  
- It can be **singly circular** (only next pointers) or **doubly circular** (both next and previous pointers).  
[View Code](https://github.com/IIEZII/Algorithms/blob/master/CircularLinkedList.py) || [Asciinema Demo](https://asciinema.org/a/KfIjFYDDEXMNrTFvwV9LqPPOy)

---

## **Queue**  
A **Queue** follows the **FIFO (First In, First Out)** principle, where elements are added at the back and removed from the front.  
[View Code](https://github.com/IIEZII/Algorithms/blob/master/queue.py) || [Asciinema Demo](https://asciinema.org/a/qe88UlryRtQFu4GvH1utaK18c)

---

## **Stack**  
A **Stack** follows the **LIFO (Last In, First Out)** principle, where elements are added and removed from the top.  
[View Code](https://github.com/IIEZII/Algorithms/blob/master/stack.py) || [Asciinema Demo](https://asciinema.org/a/YP97ZbLmWoajNkAjQEfUQ9kVg)

---

## **Heap**  
A **Heap** is a **binary tree** that maintains a specific order:  
- **Min-Heap**: The smallest element is always at the root.  
- **Max-Heap**: The largest element is always at the root.  
[View Code](https://github.com/IIEZII/Algorithms/blob/master/heap.py) || [Asciinema Demo](https://asciinema.org/a/Xhex70qccIsqAJ5Pv5l86QFFP)

---

## **Graph**  
- **Graph** is a collection of nodes (vertices) connected by edges. It can be:  
- **Directed** (edges have direction)  
- **Undirected** (edges have no direction)  

Graphs are used in shortest path algorithms, networking, and more.  
[View Code](https://github.com/IIEZII/Algorithms/blob/master/graph.py) || [Asciinema Demo](https://asciinema.org/a/w4cJ4uuae3CIJUwyzgm1nXJeV)

![image](https://github.com/user-attachments/assets/eb763eac-c9ff-425a-8873-35710a2d40ba)

1. All nodes' shortest paths to ∞, infinity, except the starting node, which is 0

![image](https://github.com/user-attachments/assets/326f81c0-b986-46d5-9ef7-d7c49a712daa)

2. A priority queue, min-heap, to always process the node with the shortest known distance first
3. For each neighbor of the current node, update the shortest distance if the new path is shorter
4. Push the updated distances into the priority queue and continue until all nodes are processed.

![image](https://github.com/user-attachments/assets/bf4af596-3608-4b10-8664-07bc955ebb9b)

Shortest paths from A: {'A': 0, 'B': 4, 'C': 5, 'D': 13, 'E': 8, 'F': 15}

---

## **Trees**  
A **Tree** is a hierarchical data structure consisting of nodes connected by edges, with one node as the root.  
- **Binary Tree**: Each node has at most **two children**.  
- **Binary Search Tree (BST)**: A binary tree where the left child contains smaller values, and the right child contains larger values.  

[View Code](https://github.com/IIEZII/Algorithms/blob/master/binary_tree.py) || [Asciinema Demo](<https://asciinema.org/a/br7xlQyAplZLw4o0qHt80zGNw>)

---

## **Usage**  
To run the implementations, clone this repository:  
```sh
git clone https://github.com/IIEZII/Algorithms.git
cd Algorithms
