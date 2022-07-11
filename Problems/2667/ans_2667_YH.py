#https://www.acmicpc.net/problem/2667
from collections import deque

def bfs(x,y, graph, visited):
    queue = deque()
    if graph[x][y] == 1:
        Num = 1
        queue.append((x,y))
        visited[x][y] = 1
        graph[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if (0 <= nx < n and 0 <= ny < n):
                if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                    Num+=1
                    visited[nx][ny]=1
                    queue.append((nx,ny))
                    graph[nx][ny] = 0
    return Num

def solve():
    global dx, dy, n, graph
    n = int(input())
    graph =[]
    visited=[[0]*n for _ in range(n)]
    dx = [-1,1,0,0] #좌,우,상,하
    dy = [0,0,1,-1]
    res = []
    for _ in range(n):
        graph.append(list(map(int,list(input()))))
    # print(graph)
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                temp = bfs(i, j, graph, visited)
                res.append(temp)
    res.sort()
    print(len(res))
    for x in res:
        print(x)
    return 

if __name__ == "__main__":
    solve()