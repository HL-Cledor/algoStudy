'''
https://www.acmicpc.net/problem/4949

스택 균형잡힌 세상
[], () 짝 맞추기
'''
import sys

class Node:
    def  __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__ (self):
        self.head = None
        self.size = 0

    def pushFirst(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        self.size += 1

    def popFirst(self):
        if self.size == 0:
            return False
        else:
            delNode = self.head
            self.head = self.head.next
            self.size -= 1
            return delNode.data
    
    def length(self):
        if self.head == 'None' or self.size == 0:
            return True
        else:
            return False

def solve():
    input = sys.stdin.readline
    while True:
        str = input()
        if str == '.' or str =='.\n':
            break

        testStr = Stack()
        check = True
        for i in str:
            if i == '(' or i == '[':
                testStr.pushFirst(i)
            elif i == ')':
                if testStr.popFirst() != '(':
                    check = False
                    break
            elif i == ']':
                if testStr.popFirst() != '[':
                    check = False
                    break
        if check != False:
            check = testStr.length()
            if check == True:
                print('yes')
            else:
                print('no')
        else:
            print('no')

if __name__ == "__main__":
    solve()