# https://www.acmicpc.net/problem/2606



def dfs(array, node, visited):
    global cnt
    visited[node] = True
    
    for i in array[node]:
        if not visited[i]:
            cnt += 1
            dfs(array, i, visited)
    return cnt
    
def solve():
    global cnt
    N = int(input())
    M = int(input())
    graph = [list(map(int,input().split())) for _ in range(N+1)]
    print(graph)
    result = 0
    cnt = 0
    visited = [False]*(N+1)
    
    result = dfs(graph,1,visited)
    print(result)

if __name__ == "__main__":
    solve()
    