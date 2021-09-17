#Circular Queue Using array

class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * self.capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def enqueue(self, data):
        if self.size == self.capacity:
            return False
        self.queue[self.tail] = data
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1
        return True

    def dequeue(self):
        if self.size == 0:
            return None
        self.size -= 1
        data = self.queue[self.head]
        self.head = (self.head + 1) % self.capacity
        return data

    def peek(self):
        if self.size == 0:
            return None
        return self.queue[self.head]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

if __name__ == '__main__':

    queue = CircularQueue(5)
    CircularQueue.enqueue(queue, 1)
    CircularQueue.enqueue(queue, 2)
    CircularQueue.enqueue(queue, 3)

    print(CircularQueue.peek(queue))
    
    print(queue.isEmpty())
    print(queue.isFull())
    print(queue.dequeue())
    print(queue.dequeue())
    

