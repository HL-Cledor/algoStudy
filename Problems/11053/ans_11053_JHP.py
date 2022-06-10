# https://www.acmicpc.net/problem/11053
# 문제 : 가장 긴 수열 조합 찾기
# 입력 : 첫째 줄 = 수열 크기 N, 둘째 줄 = 수열 A
# 출력 : 첫째 줄에 수열 A의 가장 긴 중가하는 부분 수열 길이
# 접근 : 비교를 하여서 list에 저장하면 되지 않을까?
# memo로 저장해서 연산을 줄이긴 했지만, for를 두번 써서 N^2만큼의 연산이 필요하다고 보여짐.

import sys

def seq_cnt(N):
    global A
    memo = [0]*N
    for i in range(N):
        for j in range(i):
            if A[j] < A[i]:
                memo[i] = max(memo[i],memo[j])
        memo[i] += 1
    return memo

def solve():
    global A
    
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int,input().split()))
    
    result = max(seq_cnt(N))
    print(result)

if __name__ == "__main__":
    solve()