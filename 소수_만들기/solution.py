from itertools import combinations
import math

# 에라토스테네스의 체
def check(n):
    k = math.sqrt(n)
    if n < 2: 
        return False

    for i in range(2, int(k)+1):
        if n % i == 0:
            return False
    return True


def solution(nums):
    answer = []
    tmp = list(map(list,combinations(nums,3)))
    # print(tmp)
    
    for i in tmp:
        if check(sum(i)):
            answer.append(sum(i))
    
    return len(answer)