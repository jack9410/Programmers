# 패턴 파악해야한다
# 최대공약수로 가로 세로 나누면 대각선 지나가는 사각형 패턴이 보인다

from math import gcd

def solution(w,h):

    divisor = gcd(w,h)
    
    gcd_w = w//divisor
    gcd_h = h//divisor

    # 패턴 의 가로 + 세로 -1 이 기본 개수
    pattern = gcd_h + gcd_w - 1
    # print(divisor, pattern)

    answer = w*h - pattern * divisor
    return answer