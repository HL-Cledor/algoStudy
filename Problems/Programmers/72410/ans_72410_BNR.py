'''
https://programmers.co.kr/learn/courses/30/lessons/72410

'''
def solution(new_id):
    answer = ''

    rec = new_id.lower() #1
    
    for i in rec:   #2
        if i.isalnum() == True: 
            continue
        if i == '.' or i == '-' or i =='_': 
            continue
        rec=rec.replace(i,"") 
        
    tmpRec = rec[0]
    for i in range(1, len(rec)):    #3
        if rec[i] == '.' and rec[i]==tmpRec[-1]:
            continue
        tmpRec += rec[i]   
        
    if tmpRec[0]=='.':  #4
        tmpRec = tmpRec[1:] 
    if tmpRec == "":    #5
        tmpRec = 'a'     
    if len(tmpRec)>15:  #6
        tmpRec = tmpRec[:15]
    if tmpRec[-1:] == '.':  #4
        tmpRec = tmpRec[:-1]
    if len(tmpRec)<3:   #7
        while len(tmpRec)<3:
            addchr = tmpRec[-1:]
            tmpRec += addchr
    #print(tmpRec)
    answer = tmpRec
    return answer