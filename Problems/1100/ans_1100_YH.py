#https://www.acmicpc.net/problem/1100

def solve():
    chess = []
    cnt = 0
    for _ in range(8):
        chess.append(list(input()))

    for i in range(8):
        for j in range(8):
            if (i+j)%2 == 0 and chess[i][j] == 'F':
                cnt+=1

    return print(cnt)

if __name__ =="__main__":
    solve()