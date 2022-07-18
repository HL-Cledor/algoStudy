'''
https://www.acmicpc.net/problem/2293

*DP
1. 전체 문제를 부분 문제로 잘 나누었는가
2. 부분 문제를 해결하면서 얻는 결과 값을 메모이제이션 했는가
3. 부분 문제의 점화식은 부분 문제들 사이의 관계를 커버하는가

= 가치의 합이 K원이 되는 경우의 수 -> 가치의 합이 i(1<=i<=K)되는 경우의 수로 나눠

'''
import sys


def solve():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    coin = []
    for _ in range(N):
        coin.append(int(input()))
    
    dp = [0]*(K+1)
    dp[0] =1 #동전으로 만들 수 있는 가짓 수

    for c in coin:
        for i in range(c,K+1):
            dp[i] = dp[i] +dp[i-c]
    print(dp[K])
    return
if __name__ == "__main__":
    solve()
