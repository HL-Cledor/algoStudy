# https://www.acmicpc.net/problem/5430
# 문제 : AC = 정수 배열 연산 언어, 두 가지 함수 = R(뒤집기), D(버리기)
# 입력 : 첫줄 = Test Case(T), 이후 = 각 TC별 첫줄 함수 p, 둘째줄 = 배열 갯수, 셋째줄 = 배열
# 출력 : TC의 초기값과 최종 결과값
'''
4
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
D
0
[]
'''

import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class deque:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.reverse = False
        self.size = 0
        self.errorSet = False
    
    def push(self, data):
        new_node = Node(data)
        old_node = self.tail.prev
        old_node.next = new_node
        new_node.prev = old_node
        new_node.next = self.tail
        self.tail.prev = new_node
        self.size += 1
    
    def pop_front(self):
        front_data = None
        if self.size == 0:
            front_data = -1
        else:
            front_data = self.head.data
            self.head = self.head.next 
            self.size -= 1
        if self.head == None:
            self.tail = None
        else:
            self.head.prev = None
        return front_data
    def pop_back(self):
        back_data = None
        if self.size == 0:
            back_data = -1
        else:
            back_data = self.tail.data
            self.tail = self.tail.prev
            self.size -= 1
        if self.tail == None:
            self.head = None
        else:
            self.tail.next = None
        return back_data
    
    def deque_size(self):
        return self.size
    
    def revert(self):
        self.reverse ^= True
    
    def delete(self):
        if self.reverse:
            temp = self.pop_back()
        else:
            temp = self.pop_front()
        if temp < 0:
            self.errorSet = True

    def printAll(self):
        result = []
        while True:
            if self.reverse:
                result.append(self.pop_back())
            else:
                result.append(self.pop_front())
            if result[-1] < 0:
                result.pop()
                break
        if self.errorSet:
            print("error")
        else:
            print("[", end="")
            print(",".join(str(x) for x in result), end="")
            print("]")

def solve():
    TC = int(input())
    TC_array = []
    for _ in range(TC):
        cmd = input()
        input()  # 안쓰는 input
        temp = input().replace(",", " ").replace("[", "").replace("]", "")
        data = list(map(int, temp.split()))
        TC_array.append([cmd, data])

    for val in TC_array:
        deq = deque()
        cmd, data = val
        for d in data:
            deq.push(d)
        for c in cmd:
            if c == "R":
                deq.revert()
            else:
                deq.delete()
        deq.printAll()

if __name__ == "__main__":
    solve()