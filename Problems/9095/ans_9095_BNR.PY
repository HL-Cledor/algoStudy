'''
https://www.acmicpc.net/problem/9095

n이 주어졌을 때 1,2,3의 합으로 나타내는 방법

'''
import sys

def sum_dp(n):
    dp = [0,1,2,4]
    if n>3:
        for i in range(4, n+1):
            dp.append(dp[i-1]+dp[i-2]+dp[i-3])
    print(dp[n])
    return

def solve():
    input = sys.stdin.readline
    T = int(input())
    N = []
    for _ in range(T):
        N.append(int(input()))
    
    for i in N:
        sum_dp(i)

    return

if __name__ == "__main__":
    solve()