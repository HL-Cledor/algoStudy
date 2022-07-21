#https://www.acmicpc.net/problem/1309
import sys
input = sys.stdin.readline
N = int(input())
#dp[i][0] : 이전 타일 왼쪽에 사자가 있는 경우
#dp[i][1] : 이전 타일 오른쪽에 사자가 있는 경우
#dp[i][2] : 이전 타일에 사자가 없는 경우

dp = [[1,1,1] for _ in range(N+1)]

for i in range(2,N+1):
    dp[i][0] = (dp[i-1][1]+dp[i-1][2])%9901
    dp[i][1] = (dp[i-1][0]+dp[i-1][2])%9901
    dp[i][2] = (dp[i-1][1]+dp[i-1][0]+dp[i-1][2])%9901
print(sum(dp[-1])%9901)