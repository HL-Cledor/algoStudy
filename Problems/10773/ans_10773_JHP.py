# https://www.acmicpc.net/problem/10773
# 문제 : 자못된 수를 부를때마다 0을 외쳐, 가장 최근 숫자를 제거. 이를 통해 모든 수를 받아 적은후 그 수의 합 구하기
# 입력 : 첫째줄 = 정수 K, 둘째줄~K번쨰줄 = 정수 1개씩 작성.
# 출력 : 0일 경우 최근 수를 지우고, 아닐 경우 해당 수를 씀. 이후 최종 합 출력

def solve():
    K = int(input())
    stack = []
    for _ in range(K):
        num = int(input())
        if num == 0:
            stack.pop()
        else:
            stack.append(num)
    result = sum(stack)
    print(result)

if __name__ == "__main__":
    solve()