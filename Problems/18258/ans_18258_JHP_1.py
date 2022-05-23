# https://www.acmicpc.net/problem/18258
# 문제 : 정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램 작성
# 입력 : 첫째줄 = 명령의 수 N, 둘째~N번째줄 = 명령어
# 출력 : 출력해야 하는 명령이 주어질 때마다, 한줄에 하나씩 출력

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def push(self,data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1
    
'''
import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    queue_num = []
    idx = 0
    for _ in range(N):
        cmd = input().split()
        if cmd[0] == "push":
            queue_num.append(cmd[1])
        elif cmd[0] == "size":
            print(len(queue_num)-idx)
        elif cmd[0] == "empty":
            if (len(queue_num)-idx) == 0:
                print('1')
            else:
                print('0')
        else:
            if (len(queue_num)-idx) == 0:
                print('-1')
            elif cmd[0] == "front":
                print(queue_num[idx])
            elif cmd[0] == "back":
                    print(queue_num[-1])
            elif cmd[0] == "pop":
                    print(queue_num[idx])
                    idx += 1

if __name__ == "__main__":
    solve()