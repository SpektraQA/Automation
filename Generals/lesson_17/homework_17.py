# Task 1 - Generators:


def even_numbers(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i
for num in even_numbers(10):
    print(num)

# Task 2 - Generators:

def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b
for num in fibonacci(20):
    print(num)

# Task 1 - Iterators:

class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > 0:
            self.index -= 1
            return self.data[self.index]
        else:
            raise StopIteration

for item in ReverseIterator([10, 20, 30]):
    print(item)

# Task 2 - Iterators:

class EvenNumbersIterator:
    def __init__(self, n):
        self.n = n
        self.current = -2   # починаємо з -2, щоб перше збільшення дало 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.n:
            self.current += 2
            return self.current
        else:
            raise StopIteration


for num in EvenNumbersIterator(10):
    print(num)

# Task 1 - Decorators:

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print("Аргументи:", args, kwargs)
        result = func(*args, **kwargs)
        print("Результат:", result)
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

add (3,5)

# Task 2 - Decorators:

def catch_errors(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            print("Сталася помилка", e)
            return None
    return wrapper

@catch_errors
def devide(a, b):
    return a / b

print(devide(10, 2))
print(devide(10, 0))
