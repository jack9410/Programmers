from collections import deque

def divide(p):
    n = len(p)
    left, right = 0, 0
    for idx in range(n):
        if p[idx] == '(':
            left += 1
        else:
            right +=1
        
        if left == right:
            u = p[:idx+1]
            v = p[idx+1:]
            break
    return u, v

def check_correct(p):
    n = len(p)
    stack = deque()
    for idx in range(n):
        tmp = p[idx]
        if tmp == '(':
            stack.append(tmp)
        else:
            if not stack:
                stack.pop()
            else:
                return False
    if not stack:         
        return True    

def solution(p):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
    answer = ''
    if p == '':
        return answer
    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 
    # 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
    u, v = divide(p)
    print(u, v)

    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
    if check_correct(u):
        answer += solution(v)
        # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
    
    return answer