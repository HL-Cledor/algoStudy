# https://www.acmicpc.net/problem/2580
# 문제 : 9x9 스도쿠 문제 풀기
# 제한 : PyPy3 1172ms 이하

# 접근방법 : DFS(깊이 우선 탐색) 및 백트래킹(브루트 포스) 사용
# 제한 조건이 있으므로, 유망한 숫자 검사와 재귀를 최소화 해야함.

import sys

def line_check(x,y):    
    for i in range(0,9):
        if i != y:
            if board[x][i] == board[x][y]:
                return False
    
    for j in range(0,9):
        if j != x:
            if board[j][y] == board[x][y]:
                return False     
    return True
    
def box_check(x,y):
    n_x = x//3 # 3x3
    n_y = y//3 # 3x3
    
    for i in range(n_x*3, (n_x+1)*3):
        for j in range(n_y*3, (n_y+1)*3):
            if board[i][j] == board[x][y]:
                return False
    return True

def dfs(x,y):
    global board
    
    if x == 9:
        for row in board:
            for val in row:
                print(val, end=' ')
            print()
    else:
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    for val in range(1,10):
                        if line_check(i,j) == True and box_check(i,j) == True:
                            board[i][j] = val
                            dfs(x+1,0)
                            board[i][j] = 0

def solve():
    global board
    
    input = sys.stdin.readline
    board = []
    defNum= [1,2,3,4,5,6,7,8,9]
    
    for i in range(9):
        board.append(list(map(int,input().split())))
    
    dfs(0,0) # x,y = 스도쿠 Array 위치 정보

if __name__ == "__main__":
    solve()