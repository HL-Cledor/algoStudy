#https://www.acmicpc.net/problem/1439
import sys
input = sys.stdin.readline
arr = []
arr = input()
count = 0
for i in range(len(arr)-1):
    if arr[i]!=arr[i+1]:
        count+=1

print((count)//2)