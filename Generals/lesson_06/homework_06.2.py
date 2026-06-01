word = input("Введіть слово: ")

while "h" not in word.lower():
    word = input("У слові немає літери h. Спробуйте ще раз: ")

print("Літера h знайдейјна!")