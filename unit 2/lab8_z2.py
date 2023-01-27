znak = input("Podaj znak do macierzy: ")
size = int(input("Podaj rozmiar macierzy: "))

for i in range(1, size + 1):
    print(znak * size, sep=" ")
