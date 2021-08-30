# 8/29 코테 준비
from collections import deque

def solution(s):
    answer_lst = []
    str_len = len(s)
    if str_len == 0:
        return 0
    if str_len == 1:
        return 1
    half = str_len//2
    # 단위 개수
    for unit in range(1, half + 1):
        answer = ''
        stack = deque()
        n = str_len//unit
        for k in range(n):
            unit_str = s[unit*k : unit*(k+1)]
            # 스택에 없을 때
            if not stack:
                stack.append(unit_str)
            # 스택에 있을 때
            else:
                # 같은 문자일 때
                if unit_str in stack:
                    stack.append(unit_str)
                # 다른 문자일 때
                else:
                    tmp_str = stack[0]
                    if len(stack) == 1:
                        answer += tmp_str
                    else:
                        answer += str(len(stack)) + tmp_str
                    stack.clear()
                    stack.append(unit_str)
        # 스택에 남은 문자 넣어주기
        tmp_str = stack[0]
        if len(stack) == 1:
            answer += tmp_str
        else:
            answer += str(len(stack)) + tmp_str
        # 나머지 문자 넣어주기
        answer += s[unit*(n):]

        answer_lst.append(len(answer))

    return min(answer_lst)