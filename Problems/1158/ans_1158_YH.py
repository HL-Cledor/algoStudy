#https://www.acmicpc.net/problem/1158

class CircularQueue():
    def __init__(self, MAX_QSIZE):
        self.MAX_QSIZE = MAX_QSIZE+1
        self.front = 0
        self.rear = 0
        self.queue = [0] * self.MAX_QSIZE
    def isempty(self):
        return (self.front == self.rear)
    def isfull(self):
        return (self.front == (self.rear+1) % self.MAX_QSIZE)
    def enqueue(self, data):
        if not self.isfull():
            self.queue[self.rear] = data
            self.rear = (self.rear+1)%self.MAX_QSIZE            
    def dequeue(self):
        if not self.isempty():
            temp = self.queue[self.front]
            self.front = (self.front+1)%self.MAX_QSIZE
            return temp

def solve():
    global N
    N, K = map(int, input().split())
    Queue = CircularQueue(N)
    res = []
    for i in range(1,N+1):
        Queue.enqueue(i)

    while True:
        for i in range(K-1):
            Queue.enqueue(Queue.dequeue())
        res.append(Queue.dequeue())
        # i+=1
        # if (i%N)%K == 0:
        #     res.append(Queue.dequeue())
        # else:
        #     temp = Queue.dequeue()
            
        #     Queue.enqueue(temp)
        if Queue.isempty():
            break
    print("<"+str(res)[1:-1]+">")

    return

if __name__ =="__main__":
    solve()