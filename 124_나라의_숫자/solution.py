# 참고: https://leedakyeong.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-124-%EB%82%98%EB%9D%BC%EC%9D%98-%EC%88%AB%EC%9E%90-in-python

# 3진법으로 푸는 문제
# 밑에 코드가 깔끔해서 참고했다

def solution(n):
    if n<=3:
        return '124'[n-1]
    else:
        q, r = divmod(n-1, 3)
        return solution(q) + '124'[r]
    
