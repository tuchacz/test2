# szachownica ma 64 pola
# 0 1 2 3 4
# 1 2 4 8 16  .... 2**i
sum = 0
for i in range(0, 64):
    sum += 2 ** i
print("Suma wszystkich ziaren na szachownicy: " + str(sum))

# 1 ziarno to 0,4 mg
# 1 ziarno to 0,0004 g
# 1 ziarno to 0,0000004 kg
# 1 kg = 1000g

tons = int(sum * 0.0004 / 1000 / 1000)
print(tons, "tons")
# produkcja przenicy na świecie to ok. 782 mln ton

years = round(tons / 782_000_000, 2)
print(years, "lat")

# pociąg może transportować 2200 t

trains = int(tons / 2200) + 1
print(trains)
