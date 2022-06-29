#https://www.acmicpc.net/problem/1260
from collections import deque
#breadth-First Search  
def bfs(node):
    global graph, visited
    queue = deque([node])
    visited[node] = True

    while queue:
        sNode = queue.popleft()
        print(sNode, end=' ')
        for i in graph[sNode]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
    return
#Depth-First Search
def dfs(node):
    visited[node] = True
    print(node, end=' ')
    for i in graph[node]:
        if not visited[i]:
            dfs(i)
    return

def solve():
    global graph, visited
    N,M,V = map(int,input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    for i in range(N+1):
        graph[i].sort()
    visited = [False]*(N+1)
    dfs(V)
    print('')
    visited = [False]*(N+1)
    bfs(V)

    return


if __name__ == "__main__":
    solve()


# from collections import deque
# import sys

# n, m, v = map(int, sys.stdin.readline().split())
# graph = [[] for _ in range(n+1)]
# visited = [False] * (n + 1)
# for _ in range(m):
#     a, b = map(int, sys.stdin.readline().split())
#     graph[a].append(b)
#     graph[b].append(a)
# for i in range(1, n+1):
#     graph[i].sort()


# def dfs(graph, v, visited):
#     visited[v] = True
#     print(v, end=' ')
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)


# def bfs(graph, v, visited):
#     q = deque([v])
#     visited[v] = True
#     while q:
#         v = q.popleft()
#         print(v, end=' ')
#         for i in graph[v]:
#             if not visited[i]:
#                 q.append(i)
#                 visited[i] = True


# dfs(graph, v, visited)
# print()
# visited = [False] * (n + 1)
# bfs(graph, v, visited)



# 2번 코드
# from collections import deque
# import sys
# input = sys.stdin.readline

# def dfs(x):
#     print(x, end=' ')
#     dvisited[x] = 1
#     for i in graph[x]:
#         if not dvisited[i]:
#             dfs(i)


# def bfs(x):
#     q = deque([x])
#     visited = [0] * (n+1)
#     visited[x] = 1
#     while q:
#         x = q.popleft()
#         print(x, end=' ')
#         for i in graph[x]:
#             if not visited[i]:
#                 visited[i] = 1
#                 q.append(i)


# n, m, x = map(int, input().split())
# graph = [[] for _ in range(n+1)]
# dvisited = [0]*(n+1)

# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
# for i in range(1, n+1):
#     graph[i].sort()

# dfs(x)
# print()
# bfs(x)