'''
https://programmers.co.kr/learn/courses/30/lessons/92334

'''
def solution(id_list, report, k):
    answer = [0]*len(id_list)
    warn_count = {}
    user_dic  ={}
    for i in id_list:
        warn_count[i]=0

    for i in id_list:
        user_dic[i]=[]
    set_report = list(set(report)) #중복제거

    for i in range(len(set_report)):
        user, warnedUser = map(str,set_report[i].split())
        #print(user, warnedUser)
        user_dic[user].append(warnedUser)
        warn_count[warnedUser] += 1
    
    warnedUser = []
    for key,value in warn_count.items():
        if value>=k:
            warnedUser.append(key)
    #print(warnedUser)
    
    for i in range(len(id_list)):
        for j in user_dic[id_list[i]]:
            if j in warnedUser:
                answer[i]+=1
    return answer