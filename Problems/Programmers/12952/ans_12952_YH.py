#https://programmers.co.kr/learn/courses/30/lessons/12952

def isPromising(row):
    for i in range(row):
        if (Q[i] == Q[row]) or ((row-i) == abs(Q[row]-Q[i])):
            return False
    return True
def NQueen(row):
    global cnt, N
    if row == N:
        cnt+=1
        return
    for col in range(N):
        Q[row] = col
        if isPromising(row):
            NQueen(row+1)            
                
def solution(n):
    global cnt, Q, N
    N, cnt = n, 0
    Q = [0]*n
    NQueen(0)        
    answer = cnt    
    return answer
    
if __name__=="__main__":
    print(solution(4))