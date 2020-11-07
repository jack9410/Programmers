import math

def solution(progresses, speeds):
    days = []
    answer = []
    
    n = len(progresses)
    
    for idx in range(n):
        day = math.ceil((100 - progresses[idx])/speeds[idx])
        days.append(day)
    
    print(days)
    
    tmp = 0
    distribute = 1
    
    for i in days:
        if i > tmp:
            answer.append(distribute)
            distribute = 1
            tmp = i
        else:
            distribute += 1
    answer.append(distribute)
    answer.pop(0)
            
        
        
    return answer