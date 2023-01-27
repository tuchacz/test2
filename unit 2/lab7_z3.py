import random

number = random.randint(1, 10)  # random jest "zmienną" funkcja randint losuje liczby z zakresu
msg = "Zgadnij jaką liczbę mam na myśli od 1 do 10: "
guess = int(input(msg))
if guess == number:
    print("Brawo! Dokładdnie taka liczbę miałem na myśli")
else:
    msg = "To Twoja druga szansa: "
    if number % 2 == 0:
        msg += "liczba jest parzysta: "
    else:
        msg += "nieparzysta: "
    guess = int(input(msg))
    if guess == number:
        print("Zgadłeś za drugim razem")
    else:
        msg = "To Twoja trzecia szansa: "
        if number > 5 == 0:
            msg += "moja liczba jest większa od liczby 5:"
        else:
            msg += " mniejsza lub równa od liczby 5 "
        guess = int(input(msg))
        if guess == number:
            print("Brawo! zgadłeś za 3 razem ")
        else:
            msg = "Niestety myślałem o liczbie " + str(number) + "."

