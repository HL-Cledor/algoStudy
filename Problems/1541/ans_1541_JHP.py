# https://www.acmicpc.net/problem/1541
# 문제 : +,-,()의 조합으로 식을 만들고, 괄호를 지움. 그 다음 괄호를 이용하여 식의 최소값을 만드는 프로그램 작성
# 입력 : 첫째줄 - 0~9까지 숫자와 +,-를 이용한 수식 작성
# 출력 : 첫째 줄에 정답을 출력

import sys

def solve():
    input = sys.stdin.readline
    eqn = list(map(str,input().split('-')))
    ans = 0
    
    # 가장 처음과 마지막 문자는 숫자
    for i in eqn[0].split('+'):
        ans += int(i) #input이 str형태이므로, int로 변환 필요

    # 이후 숫자의 경우, 이미 -로 분리되어 연산 처리
    for j in eqn[1:]:
        for val in j.split('+'):
            ans -= int(val) #input이 str형태이므로, int로 변환 필요
    print(ans)

if __name__ == "__main__":
    solve()