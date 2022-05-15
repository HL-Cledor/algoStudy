#https://www.acmicpc.net/problem/1157

def solve():
    temp = input()
    temp = temp.upper()
    cnt = 0
    for x in set(temp):
        if cnt > temp.count(x):
            continue
        if cnt == temp.count(x):
            res = '?'
            continue
        cnt = temp.count(x)
        res = x
        
    return print(res)

# 다른 방식의 풀이
def solve2():
    temp = input().upper()
    char_arry = [0]*26

    for x in temp:
        char_arry[ord(x)-ord('A')]+=1
    if char_arry.count(max(char_arry)) > 1:
        return print('?')
    else:
        return print(chr(ord('A')+char_arry.index(max(char_arry))))

if __name__ == "__main__":
    solve()