# 틀렸다
# 꼭 다시풀기

def board_prnt(board):
    for i in board:
        print(i)

def InBound(x,y):
    global nx, ny
    if 0 <= x < nx and 0 <= y < ny:
        return True
    else:
        return False

def check_N(check_lst, N, board):
    new_check_lst = []
    for x, y in check_lst:
        if x+N <= N and y+N <= N:
            for tmp_y in range(y, y+N):
                for tmp_x in range(x, x+N):
                    if board[tmp_y][tmp_x] == 1:
                        new_check_lst.append((x,y))
    
    return new_check_lst
            

def solution(board):
    # board_prnt(board)
    global nx, ny

    ny = len(board)
    nx = len(board[0])
    # print(nx, ny)

    check_lst = []

    for y in range(ny):
        for x in range(nx):
            if board[y][x] == 1:
                check_lst.append((x, y))

    print(check_lst)
    if check_lst:
        tmp = 1
    else:
        return 0

    while True:
        check_lst = check_N(check_lst, tmp, board)
        
        print(check_lst)
        if check_lst:
            tmp += 1
        else:
            break
    
    answer = (tmp-1)**2
    return answer


board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
solution(board)