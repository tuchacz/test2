# 64 pola
# 0 1 2 3 4
# 1 2 4 8 16  .... 2**i
sum = 0
for i in range(0,64):
    sum += 2 ** i
print("Suma wszystkich ziaren na szachownicy: " + str(sum))

