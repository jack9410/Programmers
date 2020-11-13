def solution(name):
    answer = 0
    alphaet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


    n = len(name)
    half = n//2
    # print( half)

    moves = []
    for i in name:
        tmp_move = alphaet.index(i)
        moves.append(tmp_move)

    # print(moves)

    new_dict = dict()
    for i,v in enumerate(moves):
        if i == 0 or v == 0:
            continue
        else:
            if v not in new_dict:
                new_dict[v] = [i]
            else:
                new_dict[v].append(i)
    print(new_dict)
    
    answer = moves[0]
    ans
    curr_idx = 0

    key_lst = list(new_dict.keys())
    key_lst.sort()
    print(key_lst)

    for i in key_lst:
        distance_lst = []
        for j in new_dict[i]:
            distance = abs(curr_idx - j)
            if j < half:
                distance_lst.append(distance)
            else:
                distance_lst.append(n-distance)
            print(distance_lst)
            
        






    return answer