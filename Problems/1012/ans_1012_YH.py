#https://www.acmicpc.net/problem/1012
from collections import deque

def dfs(x,y,visited,graph):
    stack = deque()
    if graph[y][x] == 1:
        stack.append((x,y))
        visited[y][x] = 1
        graph[y][x] = 0

    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if graph[ny][nx] == 1 and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    stack.append((nx,ny))
                    print(nx, ny)
                    graph[ny][nx] = 0 

    return

def bfs(x,y,visited,graph):
    queue = deque()
    if graph[y][x] == 1:
        queue.append((x,y))
        visited[y][x] = 1
        graph[y][x] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if graph[ny][nx] == 1 and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    queue.append((nx,ny))
                    print(nx,ny)
                    graph[ny][nx] = 0      
    return

def solve():
    global dx, dy, M, N
    TC = int(input())
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    for _ in range(TC):
        M, N, K = map(int, input().split())
        graph = [[0]*M for _ in range(N)]
        visited = [[0]*M for _ in range(N)]
        cnt = 0

        for _ in range(K):    
            a, b = map(int, input().split())
            graph[b][a] = 1        
        
        for i in range(M):
            for j in range(N):
                if graph[j][i] == 1:
                    bfs(i, j, visited, graph)
                    # dfs(i, j, visited, graph)
                    cnt+=1
        
        print(cnt)

    return


if __name__ == "__main__":
    solve()