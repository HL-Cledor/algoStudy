# https://www.acmicpc.net/problem/15649

import sys

def dfs(N,M):
    global visited 
    global result 

    if len(result)==M:
        print (' '.join(map(str,result)))
        return
    for i in range(1, N+1):
        if visited[i]:
            continue
        visited[i]=True
        result.append(i)
        dfs(N,M)
        result.pop()
        visited[i]=False


def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())

    global visited 
    global result 
    visited = [False]*(N+1)    
    result= []
    dfs(N,M)

if __name__ == "__main__":
    solve()