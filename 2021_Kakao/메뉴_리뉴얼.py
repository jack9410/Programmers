# 브루트 포스
# 그냥 모든 조합 다 세보고 가장 많은거 찾는다

from itertools import combinations

def solution(orders, course):
    answer = []

    for i in course:
        my_dict = dict()
        for order in orders:
            order = map(str, sorted(list(order)))
            menu_lst = combinations(order, i)
            # print(menu_lst)
            for c in menu_lst:
                tmp_course = "".join(c)
                if tmp_course in my_dict:
                    my_dict[tmp_course] += 1
                else:
                    my_dict[tmp_course] = 1
        # print(my_dict)
        if my_dict.values():
            max_order = max(my_dict.values())
        else:
            max_order = 0

        if max_order < 2:
            continue
        else:
            for k, v in my_dict.items():
                if v == max_order:
                    answer.append(k)
    
    answer.sort()
    # print(answer)
    return answer


# orders = ["XYZ", "XWY", "WXA"]
# course = [2,3,4]	
# solution(orders, course)


# 다른 사람의 풀이
# Counter 이용한다.

# from itertools import combinations
# from collections import Counter
# def solution(orders, course):
#     answer = []
#     for k in course:
#         candidates = []
#         for menu_li in orders:
#             for li in combinations(menu_li, k):
#                 res = ''.join(sorted(li))
#                 candidates.append(res)
#         sorted_candidates = Counter(candidates).most_common()
#         answer += [menu for menu, cnt in sorted_candidates if cnt > 1 and cnt == sorted_candidates[0][1]]
#     return sorted(answer)

# orders = ["XYZ", "XWY", "WXA"]
# course = [2,3,4]	
# print(solution(orders, course))