# 연도가 주어졌을 때, 윤년이면 1, 아니면 0을 춫력하는 프로그램을 작성하시오.
# 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.

def solve():
    yrs = int(input())
    
    if yrs % 4 == 0:
        if (yrs % 400 == 0):
            print("1")
        elif (yrs % 100 !=0):
            print("1")
        else:
            print("0")
    else:
        print("0")
        
if __name__ == "__main__":
    solve()    
