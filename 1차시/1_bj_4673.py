selfnum = [0]*10001
num = 0
for i in range(1,len(selfnum)):
    num = i + sum(map(int, str(i)))
    if num < len(selfnum):
        selfnum[num] = 1
            

for i in range(1,len(selfnum)):
    if selfnum[i] == 0:
        print(i)
    