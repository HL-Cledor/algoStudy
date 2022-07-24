#https://www.acmicpc.net/problem/2606

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[]*N for _ in range(N+1)]
#배열 1부터 시작
#print(graph)
for _ in range(M):
    i,j = map(int,input().split())
    graph[i].append(j)
    graph[j].append(i)
    #양방향 간선
#print(graph)
count = 0
def dfs(graph, start, visted = [1]):
    global count
    visted.append(start)
    for node in graph[start]:
        if node not in visted:
            count+=1
            dfs(graph, node,visted)
        #print("visted",visted)
        #print("start",start)
        #print("graph",graph)
    return count

print(dfs(graph,1))