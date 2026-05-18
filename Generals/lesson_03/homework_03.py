print("\ntask_01 -03\n")
alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
)
for literal in alice_in_wonderland:
    if literal == "'":
        print(literal)
print(alice_in_wonderland)
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
print("\ntask_04\n")
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea = 436402
azov_sea = 37800
together_sea = black_sea + azov_sea
print("Чорне та Азовське моря займають площу -",  together_sea, "км2")

# task 05
print("\ntask_05\n")
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
all_sklads = 375291
sklad_1_and_sklad_2 = 250449
sklad_2_and_sklad_3 = 222950
sklad_1 = all_sklads - sklad_2_and_sklad_3
sklad_2 = sklad_1_and_sklad_2 - sklad_1
sklad_3 = all_sklads - sklad_1_and_sklad_2
print( "На першому складі кількість товару:", sklad_1)
print( "На другому складі кількість товару:", sklad_2)
print( "На третьому складі кількість товару:", sklad_3)

# task 06
print("\ntask_06\n")
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
monthly_payment = 1179 #uah
payment_period = 18 #months
computer_price = monthly_payment * payment_period #uah
print("Загальна вартість комп’ютера:", computer_price, "гривень")

# task 07
print("\ntask_07\n")
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = "8019 : 8"
b = "9907 : 9"
c = "2789 : 5"
d = "7248 : 6"
e = "7128 : 5"
f = "19224 : 9"
a_ost = 8019 % 8
b_ost = 9907 % 9
c_ost = 2789 % 5
d_ost = 7248 % 6
e_ost = 7128 % 5
f_ost = 19224 % 9
print("Остача від ділення:", a, "=", a_ost)
print("Остача від ділення:", b, "=", b_ost)
print("Остача від ділення:", c, "=", c_ost)
print("Остача від ділення:", d, "=", d_ost)
print("Остача від ділення:", e, "=", e_ost)
print("Остача від ділення:", f, "=", f_ost)

# task 08
print("\ntask_08\n")

"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
pizza_large = 4 # Кількість товару
pizza_medium = 2 # Кількість товару
juice = 4 # Кількість товару
cake = 1 # Кількість товару
water = 3 # Кількість товару
cost_pizza_large = 274 # Вартість одиниці товару
cost_pizza_medium = 218 # Вартість одиниці товару
cost_juice = 35 # Вартість одиниці товару
cost_cake = 350 # Вартість одиниці товару
cost_water = 21 # Вартість одиниці товару
price_all_goods = (pizza_large * cost_pizza_large) + (pizza_medium * cost_pizza_medium) + (juice * cost_juice) + (cake * cost_cake) + (water * cost_water) # Перемножаємо кількість товару на його вартість
print(f"{price_all_goods} гривень потрібно для замовлення")

# task 09
print("\ntask_09\n")

"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
all_photos = 232
photos_per_page = 8
pages_needed = all_photos // photos_per_page
print(f"{pages_needed} сторінок потрібно, для того щоб вклеїти усі фото")


# task 10
print("\ntask_10\n")

"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance_between_cities = 1600 # В кілометрах
fuel_per_100km = 9 # необхідлно літрів на 100 км
fuel_tank_capacity = 48 # Вміст баку
total_fuel_needed = (fuel_per_100km / 100 ) * distance_between_cities
gas_station_visits = total_fuel_needed // fuel_tank_capacity
print(f"{total_fuel_needed} літрів бензину знадобиться для такої подорожі")
print(f"{gas_station_visits} щонайменше разів родині необхідно заїхати на заправку під час цієї подорожі, кожного разу заправляючи повний бак")