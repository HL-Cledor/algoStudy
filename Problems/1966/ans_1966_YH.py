#https://www.acmicpc.net/problem/1966
from collections import deque
# Queue 구현
# class Node:
#     def __init__(self,data) -> None:
#         self.data = data
#         self.next = None
#         self.prev = None
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.head = None
#         self.tail = None
#     def push(self, data):
#         self.size+=1
#         NewNode = Node(data)
#         if not self.head :
#             self.head = self.tail = NewNode
#             return
#         self.head.prev = NewNode
#         NewNode.next = self.head
#         self.head = NewNode
#     def pop(self):
#         self.size-=1
#         temp = self.tail.data
#         self.tail = self.tail.prev
#         if not self.tail:
#             self.head = None
#         return temp

def solve():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        priority = list(map(int,input().split()))
        Q = deque() #deque활용
        # Q = Queue() # 큐 구현
        for i, v in enumerate(priority):
            # Q.push((i,v))
            Q.appendleft((i,v)) 
        priority.sort()
        cnt = 0
        while Q:
            i, x = Q.pop()
            if x == priority[-1]:
                priority.pop()
                cnt+=1
                if i == M:
                    print(cnt)
                    break
            else:
                # Q.push((i,x))
                Q.appendleft((i,x))

if __name__ == "__main__":
    solve()
