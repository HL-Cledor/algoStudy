'''
https://www.acmicpc.net/problem/11054

가장 긴 바이토닉 부분 수열
'''
import sys


def bitonic(TC_List, num):
    dp_up = [1]*num
    dp_down = [1]*num
    bitonic_list = [1]*num

    for i in range(1,num):  #증가하는 수열 찾기
        for j in range(i):
            if TC_List[i]>TC_List[j]:
                dp_up[i] = max(dp_up[i], dp_up[j]+1)

    for i in range(num-1,-1,-1):    #감소하는 수열 찾기
        for k in range(num-1,i,-1):
            if TC_List[i]>TC_List[k]:
                dp_down[i] = max(dp_down[i], dp_down[k]+1)

        bitonic_list[i] = dp_up[i]+dp_down[i]-1 #자기 자신 중복제거 -1

    return max(bitonic_list)

def solve():
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    print(bitonic(arr,N))


if __name__ == "__main__":
    solve()