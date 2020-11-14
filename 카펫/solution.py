# 약수 중에서 갈색 개수와 맞는 약수 짝을 구해서 
# 각 변에 2씩 더해주면 양변의 길이가 나온다.

def solution(brown, yellow):
    answer = []

    for i in range(1, yellow+1):
        # print(i)
        if yellow % i ==0:
            second = yellow//i
            if brown == 2*(i + second) + 4:
                answer.append(second +2)
                answer.append(i+2)
                break
    return answer