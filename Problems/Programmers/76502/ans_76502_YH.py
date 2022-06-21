#https://programmers.co.kr/learn/courses/30/lessons/76502

def check(s):
    temp = []
    for x in s:
        if x == "(" or x == "[" or x=="{":
            temp.append(x)
        elif x == ")" and "(" not in temp:
            return False
        elif x == "]" and "[" not in temp:
            return False
        elif x == "}" and "{" not in temp:
            return False
        else:
            continue
    return True
    
#
def solution(s):
    answer = 0
    temp = list(s)
    for _ in range(len(s)):
        answer+=check(temp)
        temp.append(temp.pop(0))          

    
    return answer