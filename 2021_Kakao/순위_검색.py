# 실제 시험에는 정확성만 맞춘 문제
# 4 가지 항목에서 효율성을 높이는거라고 생각했으나 점수에서 효율성을 더 높여야했던 문제
# lower bound 의 개념 익히기, bisect (binary search) 익히기

from itertools import combinations
from bisect import bisect_left

def make_all_cases(tmp):
    # print(tmp)
    cases = []
    for i in range(5):
        for j in combinations([0,1,2,3], i):
            case = ''
            for idx in range(4):
                if idx not in j:
                    case += tmp[idx]
                else:
                    case += '-'
            cases.append(case)
    return cases


def solution(info, query):
    answer = []
    all_people = {}

    for tmp in info:
        split_tmp = tmp.split()
        cases = make_all_cases(split_tmp)
        for case in cases:
            if case not in all_people:
                all_people[case] = [int(split_tmp[4])]
            else:
                all_people[case].append(int(split_tmp[4]))
    
    for key in all_people.keys():
        all_people[key].sort()

    for q in query:
        tmp_answer = 0
        split_q = q.split()
        score = int(split_q[7])
        target = split_q[0] + split_q[2] + split_q[4] + split_q[6]
        # print(target)

        # 여기서 bisect 를 쓰지않으면 효율성 실패한다.
        if target in all_people:
            answer.append(len(all_people[target]) - bisect_left(all_people[target], score))
        else:
            answer.append(0)

    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info, query))