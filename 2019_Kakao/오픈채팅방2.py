def solution(record):
    answer = []
    tmp_answer = []
    user_db = dict()

    for i in record:
        tmp = i.split()
        if tmp[0] == 'Enter':
            user_db[tmp[1]] = tmp[2]
            tmp_answer.append(f'{tmp[1]} 님이 들어왔습니다.')
        elif tmp[0] == 'Leave':
            tmp_answer.append(f'{tmp[1]} 님이 나갔습니다.')
        elif tmp[0] == 'Change':
            user_db[tmp[1]] = tmp[2]

    for i in tmp_answer:
        tmp = i.split()
        answer.append(f'{user_db[tmp[0]]}{tmp[1]} {tmp[2]}')

    return answer