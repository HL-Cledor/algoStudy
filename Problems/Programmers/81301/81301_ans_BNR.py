#https://programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    answer =''
    Num_dic = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    num_value = "0123456789"

    tmp = ''
    for c in s:
        tmp = tmp+c
        if tmp in Num_dic:
            answer += str(Num_dic[tmp])
            tmp = ''
            
        elif c in num_value:
            answer += c
            tmp = ''

    return int(answer)