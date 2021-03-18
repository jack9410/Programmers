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


orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]	
solution(orders, course)