# https://www.acmicpc.net/problem/2110
# 문제 : 좌표 x_1~x_n을 가지는 N개의 집이 있을 때, C개의 공유기 설치시 공유기 사이에 최대 거리를 구하는 프로그램 작성
# 입력 : 첫째줄 = 집의 개수 N, 공유기의 개수 C, 둘째줄~N번째줄 = 집의 좌표
# 출력 : 가장 인접한 두 공유기 사이의 최대 거리 출력

import sys

def find_gap(c,home):
    min_dist = 1
    max_dist = max(home) - min(home)
    
    while min_dist <= max_dist:
        gap = (min_dist + max_dist)//2
        cnt = 1 # 가장 인접한 두 공유기 사이를 최대로 하기 위해선 첫번째 집에 설치 필요
        start = home[0]
        
        for i in range(1, len(home)):
            if home[i] - start >= gap:
                cnt += 1
                start = home[i]
        if cnt < c:
            max_dist -= 1
        else:
            min_dist += 1
            result = gap
    return result

def solve():
    input = sys.stdin.readline
    N, C = list(map(int,input().split()))
    home = []
    for _ in range(N):
        home.append(int(input()))
    home.sort()
    print(find_gap(C,home))

if __name__ == "__main__":
    solve()

'''
5 3
1
2
8
4
9
기대값 = 3
'''