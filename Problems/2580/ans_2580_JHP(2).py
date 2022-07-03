# https://www.acmicpc.net/problem/2580
# 문제 : 9x9 스도쿠 문제 풀기
# 제한 : PyPy3 1172ms 이하

# 접근방법 : DFS(깊이 우선 탐색) 및 백트래킹(브루트 포스) 사용
# 제한 조건이 있으므로, 유망한 숫자 검사와 재귀를 최소화 해야함.

import sys

def num_check(x,y):    
    defNum= [1,2,3,4,5,6,7,8,9]
    
    # (1) 가로/세로 비교
    for i in range(9):
        if board[x][i] in defNum:
            defNum.remove(board[x][i])         
        if board[i][y] in defNum:
            defNum.remove(board[i][y])     
    
    # (2) Box 확인 
    n_x = x//3 # 3x3
    n_y = y//3 # 3x3    
    for j in range(n_x*3, (n_x+1)*3):
        for k in range(n_y*3, (n_y+1)*3):
            if board[j][k] in defNum:
                defNum.remove(board[j][k])

    return defNum    

def dfs(x):
    global board
    global check
    global flag
    
    if flag:
        return
    
    if x == len(check):
        for row in board:
            print(*row) # 이렇게도 print 가능하더라고요
        flag = True
        return

    else:
        (i,j) = check[x]
        nums = num_check(i,j)
        
        for val in nums:
            board[i][j] = val
            dfs(x+1)
            board[i][j] = 0

def solve():
    global board
    global check
    global flag
    
    input = sys.stdin.readline
    board = []
    check = []
    flag = False
    
    for i in range(9):
        data = list(map(int,input().split()))
        board.append(data)
        for j in range(9):
            if data[j] == 0:
                check.append((i,j))   # 0 이 위치한 (x,y) 저장             
    
    dfs(0) # x,y = 스도쿠 Array 위치 정보

if __name__ == "__main__":
    solve()