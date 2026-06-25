
data = [
    "1,2,3,4",
    "1,2,3,4,50",
    "qwerty1,2,3"
]

def calculate_sum(numbers_string):
    numbers = numbers_string.split(",")
    total = 0

    try:
        for number in numbers:
            number = int(number)
            total += int(number)

        return total

    except ValueError:
        return "Не можу це зробити"

for item in data:
    print(calculate_sum(item))