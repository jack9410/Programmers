from itertools import permutations
import math

# 아리스토테네스의 체
def check(n):
    k = math.sqrt(n)
    if n < 2: 
        return False

    for i in range(2, int(k)+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    n = len(numbers)
    num_lst = list(numbers)
    # print(num_lst)

    answer = set()
    for i in range(1, n+1):
        # 맵기능 잘 활용하기
        perm_set = set(map(''.join, permutations(num_lst, i)))
        
        for i in perm_set:
            if check(int(i)):
                answer.add(int(i))
    # print(answer)
    return len(answer)