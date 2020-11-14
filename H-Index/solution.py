def solution(citations):
    h = 0
    citations.sort()
    answers = set()
    # print(citations)

    while True:
        if h > citations[-1]:
            break
        for i in citations:
            if i >= h:
                # print(i, h)
                h_idx = citations.index(i)
                over_h = len(citations)-h_idx
                # print(h_idx, over_h)
                if over_h >= h:
                    answers.add(h)
                    break
        h += 1
    # print(answers)
    return max(answers)