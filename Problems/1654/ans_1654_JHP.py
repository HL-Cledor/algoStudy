# https://www.acmicpc.net/problem/1654
# 문제 : 랜선 K개를 가지고 랜선 N개를 만들 수 있는 최대 길이를 구하는 문제
# 입력 : 첫째줄 - 랜선 K, N개, 둘째~K번줄 - 랜선 K의 길이
# 출력 : N개의 랜선이 가질 수 있는 최대 길이

import sys

def div_len(target,array):
    left = 1
    right = max(array)

    while left <= right:
        cnt = 0  
        mid = (left+right)//2
        
        for val in array:
            cnt += val//mid
        
        if cnt < target:
            right = mid-1
        else:   # 가장 큰 길이가 나올 때까지는 while을 계속 돌려야 함.
            left = mid+1
            ans = mid
    return ans

def solve():
    input = sys.stdin.readline
    K, N = list(map(int,input().split()))
    len_K = []
    
    for _ in range(K):
        len_K.append(int(input()))
    
    print(div_len(N,len_K))
    
if __name__ == "__main__":
    solve()