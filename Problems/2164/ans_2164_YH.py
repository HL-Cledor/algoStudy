#https://www.acmicpc.net/problem/2164
######
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
class queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    def qsize(self):
        return self.size
    def enqueue(self, data):
        if not self.size:
            NewNode = Node(data)
            self.front = NewNode
            self.rear = NewNode
            self.front.next = self.rear.prev
        else:
            NewNode = Node(data)
            self.rear.next = NewNode
            NewNode.prev = self.rear
            self.rear = NewNode
        self.size+=1
    def dequeue(self):
        if self.size > 0:
            temp = self.front.data
            self.front = self.front.next
            self.size-=1
            return temp


def solve():
    N = int(input())
    numbers = [n for n in range(1,N+1)]
    Queue = queue()
    for x in numbers:
        Queue.enqueue(x)
    while True:
        if Queue.size == 1:
            break
        Queue.dequeue()
        Queue.enqueue(Queue.dequeue())

    return print(Queue.dequeue())

if __name__ == "__main__":
    solve()