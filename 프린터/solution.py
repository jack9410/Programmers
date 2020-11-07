# 참고: https://eda-ai-lab.tistory.com/461
# 큐로 우선순위 높은거 순서대로 뺴주면서 계속 돌린다.

from collections import deque

def solution(priorities, location):
    answer = 0

    d = deque([(v,i) for i,v in enumerate(priorities)])

    while d:
        # print(d)
        item = d.popleft()
        if d and max(d)[0] > item[0]:
            d.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer