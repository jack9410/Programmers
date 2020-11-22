# 풀이 1
# functools 의 cmp_to_key 활용하기
# comparator 함수 원리 알기

import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a

    return(int(t1)>int(t2) - int(t1)<int(t2))

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer

# 풀이 2

# 문자열로 바꿔서 생각했지만 맨앞숫자가 같고 길이가 다른 수 비교할때 문제
    # 숫자가 1000이하니까 숫자 문자열을 3번 반복해줘서 비교하면된다


def solution(numbers):
    answer = ''
    
    str_num = list(map(str, numbers))
    str_num.sort(key = lambda x:x*3, reverse= True)
    # print(str_num)
    

    # 000일경우 0으로 출력되야하기때문에 int를 거쳐서 str으로 다시 바꿔준다
    return str(int(''.join(str_num)))