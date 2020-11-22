def solution(s):
    num_lst = '0123456789'
    sub_lst = []

    # print(s[1:-1])
    for i in s[1:-1]:
        if i == '{':
            tmp_lst = []
            tmp_num = ''
        elif i =='}':
            if tmp_num:
                tmp_lst.append(int(tmp_num))
            sub_lst.append(tmp_lst)
            
        elif i in num_lst:
            tmp_num += i
        elif i == ',':
            tmp_lst.append(int(tmp_num))
            tmp_num = ''
            continue
    
    sub_lst.sort(key = lambda x: len(x))
    # print(sub_lst)
    
    answer = []
    for i in sub_lst:
        for j in i:
            if j not in answer:
                answer.append(j)
    
    
    return answer