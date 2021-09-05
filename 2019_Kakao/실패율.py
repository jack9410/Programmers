def solution(N, stages):
    answer = []
    my_dict = dict()
    fail_dict = dict()

    for i in range(1, N+2):
        my_dict[i] = 0
    
    for stage in stages:
        my_dict[stage] += 1

    for i in range(N, 0, -1):
        my_dict[i] = my_dict[i] + my_dict[i+1]
    # print(my_dict)

    for i in range(1,N+1):
        if my_dict[i] == 0:
            fail_dict[i] = 0
            continue
        fail_dict[i] = stages.count(i)/my_dict[i]
    failure_lst = sorted(fail_dict.items(), key=lambda x:x[1], reverse=True)
    for i in failure_lst:
        answer.append(i[0])

    return answer