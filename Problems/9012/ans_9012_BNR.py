'''
https://www.acmicpc.net/problem/9012

스택
LIFO(Last In First Out)

올바른 괄호 문자열(VPS)이면 “YES”, 아니면 “NO”
'''
import sys

def VPS(vp):
    check_VPS = []
    for chr in vp:
        if len(check_VPS)==0:
            if chr != '(':
                return(-1)
        if chr == '(':
            check_VPS.append(chr)
        else:
            check_VPS.pop()
        # print(check_VPS)
    return len(check_VPS)

def solve():
    T=int(input())
    for _ in range(T):
        VP_input=input()
        if VPS(VP_input)==0:
            print('YES')
        else:
            print('NO')

if __name__ == "__main__":
    solve()