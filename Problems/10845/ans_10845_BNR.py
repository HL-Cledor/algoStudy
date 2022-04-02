'''
https://www.acmicpc.net/problem/10845

Queue
선입선출
'''
import sys

class Node:
    def  __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__ (self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.size = 0

    def push(self, data):
        newNode = Node(data)
        if self.size == 0:
            self.head.next = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1

    def popFirst(self):
        if self.size == 0:
            return -1
        else:
            data = self.head.next.data
            self.head = self.head.next
            self.size -= 1
            return data
    
    def Qsize(self):
        return self.size
    
    def empty(self):
        if self.size == 0:
            return 1
        else:
            return 0

    def front(self):
        if self.size == 0:
            return -1
        else:
            return self.head.next.data

    def back(self):
        if self.size == 0:
            return -1
        else:
            current = self.head
            while current.next != None:
                current = current.next
            return current.data

def solve():
    input = sys.stdin.readline
    N = int(input())
    que = Queue()
    for _ in range(N):
        order = list(input().split())
        
        if order[0] == 'push':
            que.push(int(order[1]))
        elif order[0] == 'pop':
            print(que.popFirst())
        elif order[0] == 'size':
            print(que.Qsize())
        elif order[0] == 'empty':
            print (que.empty())
        elif order[0] == 'front':
            print (que.front())
        else:
            print (que.back())

if __name__ == "__main__":
    solve()