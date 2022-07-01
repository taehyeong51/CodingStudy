table = [[0 for _ in range(6)] for __ in range(6)]
visit = [[0 for _ in range(6)] for __ in range(6)]

# print(table)

# 경로 1. 행 2개 +-, 열 1개 +-
# 경로 2. 열 2개 +-, 행 1개 +-

def move(pos):
    ini_col,ini_low = list(pos)
    ini_low = 6 - int(ini_low)
    
    AF = ['A','B','C','D','E','F']
    for idx,col in enumerate(AF):
        if ini_col == col:
            ini_col = idx
    ini_pos = list(map(int,[ini_col,ini_low]))
    dx = dy = 1
    
    move1 = [ini_col + 2*dy, ini_low + 1*dx]
    move2 = [ini_col + 2*dy, ini_low - 1*dx]
    move3 = [ini_col - 2*dy, ini_low + 1*dx]
    move4 = [ini_col - 2*dy, ini_low - 1*dx]
    move5 = [ini_col + 1*dy, ini_low + 2*dx]
    move6 = [ini_col + 1*dy, ini_low - 2*dx]
    move7 = [ini_col - 1*dy, ini_low + 2*dx]
    move8 = [ini_col - 1*dy, ini_low - 2*dx]
    
    def check(pos):
        col,low = pos
        if col > 5 or col < 0:
            return False
        elif low > 5 or low < 0:
            return False
        else:
            return True
    
    move_list = [move1,move2,move3,move4,move5,move6,move7,move8]
    possible_pos = []
    
    for idx,move_ in enumerate(move_list):
        if not check(move_):
            pass
        else:
            possible_pos.append(move_)
    ans_pos = []
    for i in possible_pos:
        ans_col,ans_low = i
        
        ans_low = 6 - ans_low
        AF = ['A','B','C','D','E','F']
        for idx,col in enumerate([0,1,2,3,4,5]):
            if col == ans_col:
                ans_col = AF[idx]
                ans = "".join([str(ans_col), str(ans_low)])
        ans_pos.append(ans) 
    return ini_col,ini_low,ans_pos

yesorno = 'Valid'

# test1 = list(input().split(" "))
# for i in range(36):
#     pos = input()
#     if i == 0:
#         before = pos
#     else:
#         if pos in move(before):
#             pass
#         else:
#             yesorno = 'Invalid'
#             break
start = ''
for i in range(36):
    pos = input()
    if i == 0:
        low,col,_ = move(pos)

        start = pos
        before = pos
        visit[low][col] = 1
        # print("pos :", pos)
    else:
        _,_,new_pos = move(before)
        low,col,_ = move(pos)
        if (pos in new_pos) and visit[low][col] == 0:
            before = pos
            visit[low][col] = 1
            
        else:
#             print(pos)
#             print(before, new_pos)

            yesorno = 'Invalid'
            break
    
_,_,last = move(pos)
if not start in last:
    yesorno = 'Invalid'
print(yesorno)