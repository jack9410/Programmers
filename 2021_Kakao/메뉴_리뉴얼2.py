# 2021-09-04
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for course_num in course:
        course_candidate_lst = dict()
        for order in orders:
            if course_num > len(order):
                continue
            else:
                course_lst = list(combinations(sorted(order), course_num))
                for candidate in course_lst:
                    tmp_course = ''.join(candidate)
                    if tmp_course in course_candidate_lst:
                        course_candidate_lst[tmp_course] += 1
                    else:
                        course_candidate_lst[tmp_course] = 1
        sorted_candidates = Counter(course_candidate_lst).most_common()
        for menu, cnt in sorted_candidates:
            if cnt == sorted_candidates[0][1] and cnt > 1:
                answer.append(menu)

    return sorted(answer)