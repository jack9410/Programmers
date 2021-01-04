from collections import deque

def solution(s):
    answer = True
    
    stack = deque()
    
    for i in s:

        # 괄호 열면 스택에 넣어준다
        if i == '(':
            stack.append(i)
        
        # 괄호닫으면
        else:
            # 스택안에 존재시 pop
            if stack:
                stack.popleft()
            # 스택안에 비었을때 false
            else:
                return False
        
    # 스택에 남아있으면 false
    if stack:
        return False    
    else:
        return True