# https://www.acmicpc.net/problem/2178
# from collections import deque

class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.prev = None
        self.next = None

class Queue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
    def append(self, data):
        self.size+=1
        NewNode = Node(data)
        if self.tail == None:
            self.tail = self.head = NewNode
            return
        self.tail.next = NewNode
        NewNode.prev = self.tail
        self.tail = NewNode
    def popleft(self):
        self.size-=1 
        temp = self.head.data
        self.head = self.head.next
        if self.head == None:
            self.tail = None       
        return temp
    
def bfs(x,y, graph, visited):
    # queue = deque()
    queue = Queue()
    queue.append((x,y))

    # while queue:
    while queue.size:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if (0 <= nx < N and 0 <= ny < M):
                if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y]+1
                    visited[nx][ny] = 1
                    queue.append((nx,ny))
    return graph[N-1][M-1]

def solve():
    global N, M, dx, dy
    N, M = map(int, input().split())
    graph = []
    
    for _ in range(N):
        graph.append(list(map(int, list(input()))))
    
    visited = [[0]*M for _ in range(N)]
    dx, dy = [-1,1,0,0], [0,0,1,-1] #좌,우,상,하

    print(bfs(0,0,graph,visited))

    return

if __name__ == "__main__":
    solve()