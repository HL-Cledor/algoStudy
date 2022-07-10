# https://www.acmicpc.net/problem/18258
# 문제 : 정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램 작성
# 입력 : 첫째줄 = 명령의 수 N, 둘째~N번째줄 = 명령어
# 출력 : 출력해야 하는 명령이 주어질 때마다, 한줄에 하나씩 출력

''' Python Singly Linked List로 구현하기 (Class 이용)
(처음)head ..... tail(맨마지막)
'''

import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class queue:

    # 초기화
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    # (1) enqueue 구현
    def push(self,data): 
        new_node = Node(data) # data 추가
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node # push이기 때문에 맨마지막 tail과 연결
            self.tail = self.tail.next
        self.size += 1

    # (2) Dequeue 구현
    def pop(self):
        pop_data = None
        if self.isEmpty() == True:
            pop_data = -1
        else:
            pop_data = self.head.data
            self.head = self.head.next # 맨 앞에 값이 뽑히고, 다음 값으로 작성
            self.size -= 1
        return pop_data
    
    # (3) size 구현
    def que_size(self):
        return self.size
    
    # (4) Front 값 출력 구현
    def front(self):
        if self.isEmpty() == True:
            print('-1')
        else:
            print(self.head.data)
    
    # (5) back 값 출력 구현
    def back(self):
        if self.isEmpty() == True:
            print('-1')
        else:
            print(self.tail.data)
    
    # (6) Empty 여부 판단
    def isEmpty(self):
        is_empty = False
        if self.head == None:
            is_empty = True
        return is_empty

def solve():
    input = sys.stdin.readline
    N = int(input())
    Q = queue()
    for _  in range(N):
        req = input().split()
        if req[0] == 'pop':
            print(Q.pop())
        elif req[0] == 'front':
            Q.front()
        elif req[0] == 'back':
            Q.back()
        elif req[0] == 'empty':
            if Q.size == 0:
                print('1')
            else:
                print('0')
        elif req[0] == 'size':
            print(Q.size)
        elif req[0] == 'push':
            Q.push(int(req[1]))

if __name__ == '__main__':
    solve()