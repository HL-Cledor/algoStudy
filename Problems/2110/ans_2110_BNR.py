'''
https://www.acmicpc.net/problem/2110

가장 인접한 두 공유기 사이의 최대 거리
'''
import sys

def bs(array,W):
    start = 1
    end = array[-1] - array[0]
    while start<=end:
        mid = (start+end)//2
        current = array[0]
        cnt = 1
        for i in range(1, len(array)):
            if array[i]>= current + mid:
                cnt+=1
                current = array[i]

        if cnt >=W:
            start = mid + 1
            result = mid
        else:
            end = mid -1
    return result

def solve():
    input = sys.stdin.readline
    N, wifi_N = map(int, input().split(' '))
    home = []
    for _ in range(N):
        home.append(int(input()))
    home.sort()
    print(bs(home,wifi_N))
    

if __name__ == "__main__":
    solve()