# 참고: https://ychae-leah.tistory.com/96

# 답을 보면 정말 쉬운 문제지만 제대로 이해하는데 오래걸렸던 문제
# 또 풀이도 무식하게 풀어도 되지만 생각해보면 훨씬 간단한 풀이를 생각할 수 있는 문제

def solution(citations):
    n = len(citations)
    citations.sort()
    print(citations)

    for i in range(n):
        if citations[i] >= n-i:
            # 논문이 인용된 횟수(h번 이상) >= 인용된 논문의 개수(h개 == h번)
            return n-i
    return 0