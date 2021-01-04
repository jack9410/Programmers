def grid_prnt(grid):
    for i in grid:
        print(i)

def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret

def find_hole(lock):
    n = len(lock)
    key_hole = []
    for i in range(n):
        for j in range(n):
            if lock[i][j] == 0:
                key_hole.append((j,i))
    return key_hole

def find_key(key):
    n = len(key)
    key_hole = []
    for i in range(n):
        for j in range(n):
            if key[i][j] == 1:
                key_hole.append((j,i))
    return key_hole

# def inBound(x,y):


def move_key(key_hole, key_lst):
    x, y = key_hole[0]
    answer = []

    for tmp in key_lst:
        tmp_x, tmp_y = tmp
        dx = x - tmp_x
        dy = y - tmp_y
        moved_lst = [ (tmp_x + dx, tmp_y+dy) for tmp_x, tmp_y in key_lst]

        # print(moved_lst)      
        for i in moved_lst:
            x, y = i
            if x<0 or x>=n or y<0 or y>=n:
                moved_lst.remove((x,y))
        # print(moved_lst)

        if moved_lst == key_hole:
            return True




def solution(key, lock):
    global n
    n = len(key)
    key_hole = find_hole(lock)
    # print(key_hole)
    # print()

    for _ in range(4):
        key = rotate_90(key)
        key_lst = find_key(key)
        # print(key_lst)
        if move_key(key_hole, key_lst):
            return True

    return False