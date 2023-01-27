import random

counter = 1
number = random.randint(1,10)  # losowanie z przedziału calkowitego
guess = int(input("Zgadnij jaką liczbę mam na myśli (1-10): "))

while number!= guess:
    guess = int(input("NIE TO NIE TA, spróbuj jeszcze raz: "))
    counter += 1   # licznik liczący ilośc prób, jest powiększany w momencie wejścia w pętle

print("Brawo! Udało Ci się za " + str(counter) + " razem.")

