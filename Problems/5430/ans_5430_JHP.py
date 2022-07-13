# https://www.acmicpc.net/problem/5430
# 문제 : AC = 정수 배열 연산 언어, 두 가지 함수 = R(뒤집기), D(버리기)
# 입력 : 첫줄 = Test Case(T), 이후 = 각 TC별 첫줄 함수 p, 둘째줄 = 배열 갯수, 셋째줄 = 배열
# 출력 : TC의 초기값과 최종 결과값

import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    TC = int(input())
    
    for _ in range(TC):
        cmd = list(input().rstrip())
        N = int(input())
        data = list(input().rstrip().strip('[').strip(']').split(','))
        que = deque(data)
        rev_cnt = 0
        err_flg = False
        result = ''

        for c in cmd:
            if c == 'R':
                rev_cnt += 1
            elif c == 'D':
                if que == deque([]) or que == deque(['']):
                    err_flg = True
                else:
                    if rev_cnt % 2 == 0: # reverse 횟수가 짝수 일 때
                        que.popleft()
                    else:
                        que.pop()
        if err_flg == True:
            print('error')
        else:
            if rev_cnt % 2 == 1:
                que.reverse() # 홀수 일 경우에는 reverse된 결과 출력 필요
            result = '['+','.join(que)+']'
            print(result)

if __name__ == "__main__":
    solve()