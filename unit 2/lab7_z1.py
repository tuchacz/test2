# program sprawdza czy pierwiastek kwadratowy z liczby całkowitej jest także liczbą całkowitą
a = float(input("Podaj liczbę: "))

print("Liczba jest: ", a)

result = a ** 0.5

print(result)

if result % 1 == 0:
    print("Liczba jest całkowita")
else:
    print("Liczba nie jest całkowita")