list_value = list(range(10))

summa = 0

for number in list_value:
    if number % 2 == 0:
        summa += number
        print(summa)
