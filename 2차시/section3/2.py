import re
string = 'Akdj0Gk1dgdgdAGSGAG3DGGA45GAGADGDGdjADG2SDGkdj0f'

num = re.compile('[0-9]')
res = ''
for s in string:
    if num.match(s):
        res += s

res = int(res)
print(res)
cnt = 1
ans = 1
for i in range(2,res):
    while res % i == 0 :
        cnt += 1
        res = res / i
    
    ans *= cnt
    cnt = 1
    if res < 2:
        break

print(ans)
