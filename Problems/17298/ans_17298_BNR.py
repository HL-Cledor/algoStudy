# https://www.acmicpc.net/problem/17298

import sys

class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None

class linked_Stack(object):
    def __init__(self):
        self.head = None
        self.size = 0
        self.cnt = 0
        self.tail = None

    def pushFirst(self,data):
        addNode = Node(data)
        addNode.next = self.head
        self.head = addNode
        self.size += 1

    def delFirst(self):
        delNode = self.head
        self.head = delNode.next
        delNode = None
        self.size -= 1

    def findRBV(self):
        node = self.head
        comnode = node.next

        while node.next != None:
            if node.data < comnode.data:
                print(comnode.data, end=' ')
                node = node.next
                comnode = node.next
            else:
                if comnode.next == None:
                    print(-1, end=' ')
                    node = node.next
                    comnode = node.next
                else:
                    comnode = comnode.next 
        return -1      #끝 값 처리

def solve():
    input = sys.stdin.readline
    N = int(input())
    TC = list(map(int,input().split()))
    updateStack = linked_Stack()

    for num in range(N-1,-1,-1):
        updateStack.pushFirst(TC[num])
    print(updateStack.findRBV(), end=' ')

if __name__ == "__main__":
    solve()