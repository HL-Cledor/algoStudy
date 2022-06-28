#https://www.acmicpc.net/problem/2156
import sys

#Bottom-Up1
def solve1(): #너무 어렵게 푼것 같음.
    input = sys.stdin.readline
    N = int(input())
    wine = [int(input()) for _ in range(N)]
    dp = [[0,0,0,0] for _ in range(N+1)]
    dp[1]= [0,wine[0],0,0]

    for i in range(2,N+1):
        dp[i][0] = dp[i-1][1]+wine[i-1] #끝 O O 경우
        dp[i][1] = max(dp[i-1][3], dp[i-1][2])+wine[i-1] #끝 X O 경우
        dp[i][2] = max(dp[i-1][0], dp[i-1][1]) #끝 O X 경우
        dp[i][3] = max(dp[i-2][0], dp[i-2][1], dp[i-1][2]) #끝 x X 경우
    print(max(dp[-1]))

#Bottom-Up2    
def solve2():
    input = sys.stdin.readline
    N = int(input())
    wine = [int(input()) for _ in range(N)]
    if N < 3: print(sum(wine)) # Index Error 회피 
    else:
        dp = [wine[0], wine[0]+wine[1], max(wine[0]+wine[1], wine[0]+wine[2], wine[1]+wine[2])] # 초기값
        for i in range(3,N):
            dp.append(max(dp[i-3]+wine[i-1]+wine[i], dp[i-2]+wine[i], dp[i-1]))
            #(빈칸+연속 2개로 끝날 때, 빈칸+한개로 끝날 때, 빈칸으로 끝날 때)
        print(dp[-1])

if __name__=="__main__":
    solve2()
    