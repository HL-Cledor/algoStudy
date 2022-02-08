# https://www.acmicpc.net/problem/1003
# 동적 계획법 - 패턴을 찾아서 패턴을 활용할 수 있는 방법 고려
# 재귀 호출되는 횟수를 줄여 좀더 효율성이 높고, 빠른 코딩을 구현하고자 함. (어렵다..)

def fibonacci(x):
    if x == 0:
        return dp_num[0]
    elif x == 1:
        return dp_num[1]
    else:
        for i in range(2, x+1):
            dp_num[i] = [dp_num[i-1][0]+dp_num[i-2][0], dp_num[i-1][1]+dp_num[i-2][1]]
        return dp_num[i]

def solve():
    global dp_num

    test_n = int(input())
    result = dict()
    dp_num = dict()
    
    dp_num[0] = [1,0] # zero가 나오는 table 값
    dp_num[1] = [0,1] # one이 나오는 table 값
    
    for i in range(test_n):
        N = int(input())
        result[i]=fibonacci(N)
    
    for j in range(test_n):
        print(*result[j])
    
if __name__ == "__main__":
    solve()
