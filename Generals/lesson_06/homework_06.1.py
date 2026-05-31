# Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False. Строку отримати за допомогою функції input()
str_1 = input()
unique_symbols = set(str_1)
long_unique_symbols = len(unique_symbols)
if long_unique_symbols >10:
    print(True)
else:
    print(False)
