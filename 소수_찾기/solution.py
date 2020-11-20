from itertools import permutations

def solution(numbers):
    n = len(numbers)
    num_lst = list(numbers)
    print(num_lst)

    num_set = set()
    for i in range(1, n+1):
        perm_lst = list(permutations(num_lst, i))
        print(perm_lst)
    
    answer = 0
    return answer