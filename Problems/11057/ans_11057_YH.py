#https://www.acmicpc.net/problem/11057

def solve():
    N = int(input())
    dp = [[0 for _ in range(10)] for _ in range(1001)] #dp[i][j] = 자릿수 i인 수 중 j로 끝나는 수
    dp[1] = [1 for _ in range(10)]
    for i in range(2,N+1):
        for j in range(10):
            for k in range(j+1):
                dp[i][k]+=dp[i-1][j]
                print(dp[i][k],dp[i-1][j])
    return print(sum(dp[N])%10007)

def solve2():
    n = int(input()) 
    num = [1]*10 
    for _ in range(n-1): 
        for j in range(1, 10):
            num[j] += num[j-1] 
    print(sum(num)%10007)

if __name__ == "__main__":
    solve()