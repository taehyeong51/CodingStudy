import sys
import math

for i in range(int(input())):
    word = input().upper()
    if word[:len(word)//2] == word[math.ceil(len(word)/2):][::-1]:
        print('#'+str(i+1)+" YES")
    else:
        print('#'+str(i+1)+" NO")


