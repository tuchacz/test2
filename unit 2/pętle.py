# wyświetl wszystkie cyfry od 1 do 10 włącznie
"""
i = 0
while i < 10:  # jest powiększane za każdym razem
    print(i, end=" ")
    i += 1
"""
"""
alternatywny zapis 
for i in range(0, 10):  # i < 10   0,1,2..,9
    print(i, end=" ")
"""

"""
for i in range(10): # range (0,10,1) zawsze "i" w tym przypadku zaczyna się od zera
    print(i)

for i in range(0, 10, 1): # range (0,10,1)
    print(i)
"""
"""
for i in range(3,10): #iterowanie od 3
    print(i)
"""

"""
#początek i =2
# dopóki i<10
#skaczemy co 3
for i in range(2,10,3): #iterowanie od 2 z przeskokiem 3
    print(i)
"""

"""
# program inkrementuje w dół
for i in range(9, -2, -1): #iterowanie od 9 z przeskokiem -1
    print(i)

#początek i =2
# dopóki i>6
#skaczemy co -1
# program inkrementuje w dół
for i in range(9, 6, -1): #iterowanie od 9 z przeskokiem -1
    print(i)

"""

for i in range(5):
    print(i)
else:
    print("Koniec pętli ....")

#breakowanie przerywanie pętli
for i in range(5):
    print(i)
    if i==3:
        break
else:
    print("Koniec pętli ....")

number = int(input("Podaj rozmiar "))
char = input("podaj znak: ")
for i in range(number):
    for j in range(number):
        print(char, end=" ")
    print()

# szachownica ma 64 pola
# 0 1 2 3 4
# 1 2 4 8 16  .... 2**i
sum = 0
for i in range(0,64):
    sum += 2 ** i
print("Suma wszystkich ziaren na szachownicy: " + str(sum))

# 1 ziarno to 0,4 mg
# 1 ziarno to 0,0004 g
# 1 ziarno to 0,0000004 kg
# 1 kg = 1000g

tons = int()