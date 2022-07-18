'''
https://www.acmicpc.net/problem/9465


'''
import sys

def solve():
    input = sys.stdin.readline
    TC_N = int(input())

    for _ in range(TC_N):
        N = int(input())
        STK = []
        STK.append(list(map(int,input().split(' '))))
        STK.append(list(map(int,input().split(' '))))
        
        if N>1:
            STK[0][1] = STK[0][1] + STK[1][0]
            STK[1][1] = STK[1][1] + STK[0][0]

            for i in range(2,N):
                STK[0][i] = max(STK[1][i-2], STK[1][i-1]) +STK[0][i]
                STK[1][i] = max(STK[0][i-2], STK[0][i-1]) +STK[1][i]

        print(max(STK[0][N-1], STK[1][N-1]))

if __name__ == "__main__":
    solve()