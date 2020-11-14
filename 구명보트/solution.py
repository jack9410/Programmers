# 항상 문제 조건을 잘읽자
# 최고 2명씩 탈 수 있는게 포인트
# 항상 최고 몸무게와 최저 몸무게랑 비교해서 같이 태울수 없으면 혼자 태운다


def solution(people, limit):
    answer = len(people)
    people.sort(reverse = True)
    # print(people)
    
    # 투포인터
    s,e = 0, len(people)-1
    
    while s < e : 
        # 짝이 지어지면 횟수 한번 뺀다.
        if people[s] + people[e] <= limit :
            e-=1
            answer-=1
        s+=1
    
    return answer