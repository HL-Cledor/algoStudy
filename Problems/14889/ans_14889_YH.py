#https://www.acmicpc.net/problem/14889

N = int(input())
S = []
Choice = [0]*N
res = 100

def dfs(idx):
    global res
    if idx == N//2:
        START, LINK = 0, 0
        for i in range(N):
            for j in range(N):
                if Choice[i] and Choice[j]:
                    START+=S[i][j]
                elif not Choice[i] and not Choice[j]: 
                    LINK+=S[i][j]
        res = min(res, abs(START - LINK))  
        return 
    
    for i in range(idx, N):
        if not Choice[i]:
            Choice[i]=1
            dfs(idx+1)
            Choice[i]=0

def solve():    
    for _ in range(N):
        S.append(list(map(int, input().split())))        
    
    dfs(0)
    return print(res)

#dfs로 풀기
if __name__ =="__main__":
    solve()
        