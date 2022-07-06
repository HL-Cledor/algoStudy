#https://programmers.co.kr/learn/courses/30/lessons/62048

# 풀이 참조하여 최대 공약수(gcd)를 찾는 유클리드 호제법 이용한 풀이
# 최대 공약수 단위로 패턴(직선이 지나는 블럭 모양)이 있으며, 다음 패턴과 한 점으로 연결되어 있음
# 한 패턴의 start에서 end까지 가는 길은 수평길이 + 수직길이 - 공통 부분
# 패턴 : (w/gcd) + (h/gcd) - 1

def solution(w,h):
    answer = 1
    if w >=h:
        a, b = w, h
    else:
        a, b = h, w
    while b:
        c = a % b
        a = b
        b = c
    answer = w*h -(w + h - a)
    
    return answer