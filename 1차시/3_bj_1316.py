import sys
N = int(input())
cnt = 0
for _ in range(N):
    word = input()
    for w in set(word):
        wcnt = word.count(w)
        if wcnt > 1:
            wo = word[word.find(w):word.find(w)+wcnt]
            if wo.count(w) != wcnt:
                cnt +=1
                break
print(N-cnt)