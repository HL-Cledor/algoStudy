# https://www.acmicpc.net/problem/12015
# 문제 : 가장 긴 증가하는 부분 수열2
# 입력 : 첫째줄 - 수열 A의 크기 N, 둘째줄 - 수열 A를 이루는 Ai
# 출력 : 가능 긴 부분 수열의 길이

def bs(LIS,length,target):
    start = 0
    end = length-1
    while start < end:
        mid = (start+end)//2
        if target <= LIS[mid]:
            end = mid
        else:
            start = mid + 1
    LIS[end] = target

def solve():
    N = int(input())
    A= list(map(int,input().split()))
    LIS = []
    
    for i in range(0,N): # dp
        if i == 0:
            LIS.append(A[i])
            
        if LIS[-1] > A[i]:
            bs(LIS,len(LIS),A[i]) # binary search 사용 
        elif LIS[-1] == A[i]:
            continue
        else:
            LIS.append(A[i])
    print(len(LIS))

if __name__ == "__main__":
    solve()