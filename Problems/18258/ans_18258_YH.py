#https://www.acmicpc.net/problem/18258
#https://one-step-a-day.tistory.com/112

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class Queue:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.qsize = 0
    
    def enqueue(self,data):
        NewNode = Node(data)
        if self.front() is None:
            self.head = NewNode
            self.tail = NewNode
            self.head.next = self.tail
            print(1)
            print(2)
        else:
            self.tail.next = NewNode 
            self.tail = NewNode
            self.qsize+=1
        # print(self.front())
        print(self.front() is None)
        


    def dequeue(self):
        if self.isempty():
            return -1
        else:
            data = self.head.data
            self.head = self.head.next
            self.qsize-=1
            return data

    def isempty(self):
        if self.qsize:
            return 0
        return 1

    def front(self):
        if self.isempty():
            return -1
        return self.head.data
    
    def back(self):
        if self.isempty():
            return -1
        return self.tail.data
    
    def size(self):
        return self.qsize


def solve():
    N = int(input())
    queue = Queue()
    for _ in range(N):
        cmd = input().split()
        if cmd[0] == "push":
            queue.enqueue(int(cmd[1]))
            print(int(cmd[1]))
        elif cmd[0] == "pop":
            print(queue.dequeue())
        elif cmd[0] == "size":
            print(int(queue.size()))
        elif cmd[0] == "empty":
            print(queue.isempty())
        elif cmd[0] == "front":
            print(queue.front())
        elif cmd[0] == "back":
            print(queue.back())
        else :
            pass

    return

if __name__ == "__main__":
    solve()