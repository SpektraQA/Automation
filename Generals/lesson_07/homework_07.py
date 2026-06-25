# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    multiplier = 1

    while True:
        result = number * multiplier

        if result > 25:
            break

        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        multiplier += 1


multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_two_numbers(a, b):
    return a + b


print(sum_two_numbers(3, 5))


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def calculate_average(numbers):
    return sum(numbers) / len(numbers)


print(calculate_average([1, 2, 3, 4, 5]))
# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(text):
    return text[::-1]


print(reverse_string("Python"))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def find_longest_word(words):
    longest_word = words[0]

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word


print(find_longest_word(["cat", "elephant", "dog"]))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    return str1.find(str2)


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # -1 # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
# task 7
def has_more_than_10_unique_symbols(text):
    """
    Checks whether the string contains more than 10 unique characters.
    Returns True if yes, otherwise False.
    """
    unique_symbols = set(text)
    return len(unique_symbols) > 10


print(has_more_than_10_unique_symbols("hello world"))


# task 8
def sum_even_numbers(numbers):
    """
    Returns the sum of all even numbers in the list.
    """
    total_sum = 0

    for number in numbers:
        if number % 2 == 0:
            total_sum += number

    return total_sum


print(sum_even_numbers([1, 2, 3, 4, 5, 6]))


# task 9
def get_strings_from_list(items):
    """
    Returns a new list containing only string values.
    """
    string_items = []

    for item in items:
        if isinstance(item, str):
            string_items.append(item)

    return string_items


print(get_strings_from_list(['1', '2', 3, True, 'False', 5, '6']))


# task 10
def contains_h(word):
    """
    Checks whether the word contains the letter 'h' or 'H'.
    Returns True if found, otherwise False.
    """
    return "h" in word.lower()


print(contains_h("Hello"))
print(contains_h("Python"))