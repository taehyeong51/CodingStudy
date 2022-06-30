card = [str(i) for i in range(1,21)]

a = [13,2,1,3,1,1,11,5,1,1]
b = [17,19,2,19,1,9,16,6,3,9]

for s,e in zip(a,b):
    now = card[s-1:e] 
    card = card[:s-1] + now[::-1] + card[e:]
    
print(" ".join(card))
if " ".join(card) == "19 1 2 4 3 5 8 7 6 9 15 16 17 12 11 10 14 13 18 20":
    print("ok")