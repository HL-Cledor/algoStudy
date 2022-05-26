# https://www.acmicpc.net/problem/2839
# 문제 : N kg의 설탕을 배달해야 할 때, 3kg/5kg 봉투를 이용하여 최소한의 봉투 찾기
# 입력 : N kg의 설탕
# 출력 : 최소 배달 봉투 수 (없을 경우에는 -1 출력)

import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    result = 0
        
    while N >= 0:
        if N % 5 == 0:
            result += N//5
            break
        else:
            N -= 3
            result += 1
    
    if N < 0:
        print(-1)
    else:
        print(result)

if __name__ == "__main__":
    solve()