# 3! =1*2*3

number = 5  # 1*2*3*4*5
factorial = 1

for i in range(1, number + 1):
    factorial *= i
print(factorial)

#alternatywnie za pomocą while

number = 5  # 1*2*3*4*5
factorial = 1

while number:
    print(number, factorial)
    factorial *= number
    number -= 1

print(factorial)
