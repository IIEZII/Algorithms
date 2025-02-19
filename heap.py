import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, info):
        heapq.heappush(self.heap, info)

    def remove_min(self):
        if self.heap:
            return heapq.heappop(self.heap)
        return None

    def display(self):
        print("Heap:", self.heap)

print("\nTask Scheduler (Min Heap):")
heap = MinHeap()
heap.insert(3)
heap.insert(1)
heap.insert(4)
heap.insert(2)
heap.display()
print("Removed Min:", heap.remove_min())
heap.display()
