znak = input("Podaj znak do prostokątu: ")
kol = int(input("Podaj liczbę kolumn do prostokątu: "))
wiersz = int(input("Podaj liczbę wierszy do prostokątu: "))

print("Rysuje prostokąt")
print((znak * kol + "\n") * wiersz)
