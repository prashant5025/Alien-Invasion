class Queue(object):

    def __init__(self,size):
        self.queue = []
        self.size = size

    def __str__(self):
        myString =''.join(str(i) for i in self.queue)
        return myString

    def enqueue(self,item):
        if len(self.queue) < self.size:
            self.queue.append(item)
        else:
            print("Queue is full")


    def dequeue(self):
        if len(self.queue) > 0:
            self.queue.pop(0)
        else:
            print("Queue is empty")

    def isEmpty(self):
        return self.queue == []

    def isFull(self):
        return len(self.queue) == self.size

    def peek(self):
        
        if(self.isEmpty() == False):
            return self.queue[0]

    def size(self):
        return len(self.queue)


if __name__ == '__main__':
    myQueue = Queue(5)
    myQueue.enqueue(1)
    myQueue.enqueue(2)
    myQueue.enqueue(3)
    myQueue.enqueue(4)
        

    print(myQueue)

    myQueue.enqueue(20)

    myQueue.dequeue()
    print(myQueue)
        
    