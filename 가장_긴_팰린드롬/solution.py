def solution(s):
    odd_answer, even_answer = 1,1
    N = len(s)
    # 홀수일 때
    for idx in range(1,N-1):
        
        if s[idx-1] == s[idx+1]:
            left, right = idx-1, idx+1
            tmp_odd_answer = 1
            
            while s[left] == s[right]:
                tmp_odd_answer += 2 
                if left == 0 or right == N-1:
                    break
                left -= 1
                right += 1
            odd_answer = max(odd_answer, tmp_odd_answer)


    # 짝수일 때
    for idx in range(1,N):
        if s[idx] == s[idx-1]:
            # print('인덱스',idx)
            tmp_even_answer = 0
            left, right = idx-1, idx

            while s[left] == s[right]:
                # print(s[left], s[right])
                tmp_even_answer += 2 
                # print(left, right)
                if left == 0 or right == N-1:
                    break
                left -= 1
                right += 1
            even_answer = max(tmp_even_answer, even_answer)

    answer = max(odd_answer, even_answer)
    return answer
