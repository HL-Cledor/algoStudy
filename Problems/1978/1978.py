"""
Problem: https://www.acmicpc.net/problem/1978

소수 찾기
"""

TCnum = int(input())
TC = list(map(int, input().split()))

cnt = 0
for i in TC:
    n=2 
    if i == 1:
        cnt = cnt
    elif i ==2:
        cnt = cnt + 1
    else:
        while n < i:
            if i % n == 0:
                break
            if n == i-1:
                cnt = cnt +1
            n = n + 1

print(cnt)
