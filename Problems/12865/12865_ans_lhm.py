#https://www.acmicpc.net/problem/12865
import sys
input = sys.stdin.readline

N,K = map(int, input().split())

dp = [[0]*(K+1) for _ in range(N+1)]
items = [[0,0]]+[[*map(int,input().split())] for _ in range(N)]

# items[i][1] i번째 물건의 가치
# items[i][0] i번째 물건의 무게


for i in range(1,N+1):
    for j in range(1,K+1):
        if j < items[i][0]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], items[i][1]+dp[i-1][j-items[i][0]])

print(dp[N][K])