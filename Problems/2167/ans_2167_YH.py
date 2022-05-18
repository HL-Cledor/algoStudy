#https://www.acmicpc.net/problem/2167

def solve(): #python 시간초과 / pypy3 통과
    N, M = map(int, input().split())
    arry = [list(map(int,input().split())) for _ in range(N)]
    
    K = int(input())
    for _ in range(K):
        i,j,x,y = map(int, input().split())
        i,j,x,y = i-1,j-1,x-1,y-1
        res = 0
        for u in range(i,x+1):
            for w in range(j,y+1):
                res+=arry[u][w]
                print(arry[u][w])
        print(res)

def solve2(): # python 통과
    N, M = map(int, input().split())
    arry = [list(map(int, input().split())) for _ in range(N)]

    K = int(input())
    dp = [[0] * (M+1) for _ in range(N+1)] #dp[x][y] - x by y 배열의 요소 총 합

    for i in range(1, N+1):
        for j in range(1, M+1):
            dp[i][j] = arry[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]

    for _ in range(K):
        i, j, x, y = map(int, input().split())
        print(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1])

if __name__ =="__main__":
    solve2()