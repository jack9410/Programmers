def solution(record):
    id_list = {}
    temp_answer = []
    answer = []

    for i in record:
        temp = i.split()
        if temp[0] == ('Enter'):
            id_list[temp[1]] = temp[2]
            temp_answer.append(temp[1] + ' 님이 들어왔습니다.')
        elif temp[0] == 'Leave':
            temp_answer.append(temp[1] + ' 님이 나갔습니다.')
        elif temp[0] == 'Change':
            id_list[temp[1]] = temp[2]

    for i in temp_answer:
        temp = i.split()
        answer.append(id_list[temp[0]] + temp[1] + ' ' + temp[2])
    
    return answer