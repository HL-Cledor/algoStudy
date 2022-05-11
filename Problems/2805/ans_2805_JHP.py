# https://www.acmicpc.net/problem/2805
# 문제 : 나무 N개에서 M미터 길이의 나무를 가져가려 할 때, 절단기의 최대 높이을 구하는 프로그램
# 입력 : 첫째 줄 = 나무의 수 N, 나무의 길이 M, 둘째 줄 = 나무의 높이
# 출력 : M미터의 나무를 가져가기 위한 최대 절단기 설정 높이

import sys

def div_tree(target, array_len):
    left = 0
    right = max(array_len)
    max_len = 0
    
    while right - left > 1:
        total_len = 0
        mid = (left+right)//2        
        
        for val in array_len:
            if val > mid: # val % target으로 했을 경우, 
                total_len += val - mid 

        if total_len > target: 
            left = mid
            max_len = mid   # 남은 길이가 target보다 큰 경우에도 최대 길이는 유효함. (이 부분이 없어도 예제는 모두 정답이지만, 반례가 있음.)  
        elif total_len < target:
            right = mid 
        else:
            max_len = mid   # 딱 맞게 떨어지는 경우,
            break
    return max_len

def solve():
    input = sys.stdin.readline
    N, M = list(map(int,input().split()))
    len_tree = list(map(int,input().split()))

    print(div_tree(M,len_tree))
    
if __name__ == "__main__":
    solve()