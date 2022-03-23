'''
https://www.acmicpc.net/problem/10845

Queue
선입선출
'''
import sys

class Queue:
    def __init__ (self):
        self.Q = []

    def push (self, val):
        self.Q.append(val)

    def empty (self):
        if len(self.Q)==0:
            return 1
        return 0 
    
    def size (self):
        return len(self.Q)
    
    def pop(self):
        if len(self.Q)==0:
            return -1
        else:
            return self.Q.pop(0)
    
    def front (self):
        if len(self.Q)==0:
            return -1
        else:
            return self.Q[0]
    
    def back (self):
        if len(self.Q)==0:
            return -1
        else:
            return self.Q[-1]

def solve():
    input = sys.stdin.readline
    N = int(input())
    que = Queue()
    for _ in range(N):
        order = list(input().split())
        
        if order[0] == 'push':
            que.push(int(order[1]))
        elif order[0] == 'pop':
            print(que.pop())
        elif order[0] == 'size':
            print (que.size())
        elif order[0] == 'empty':
            print (que.empty())
        elif order[0] == 'front':
            print (que.front())
        else:
            print (que.back())

if __name__ == "__main__":
    solve()