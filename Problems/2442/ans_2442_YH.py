#https://www.acmicpc.net/problem/2442

def solve():
    N = int(input())
    for i in range(1,N+1):
        temp = " "*(N-i)
        star = "*"*(2*i-1)
        res = temp+star
        print(res)

    return

if __name__ == "__main__":
    solve()