#----Функції----
#❌ Погано:
a = 10
b = 20
print(a + b)

a = 5
b = 7
print(a + b)

#✅ Нормально:

def add(a, b):
    return a + b
add(4,6)
# Функція =
# перевикористання
# читабельність
# тестування
# масштабування
# Якщо код повторюється — це функція. Без обговорень.

def greet(name: str) -> str:
    return f"Hallow {name}"
result = greet("den")
print(result)


# Розбираємо:
# def — оголошення
# name — параметр
# return — результат (без нього → None)
# -> str — type hint (поки не обовʼязково)

#---Return vs print (критично важливо)
#❌ Погано:
def add(a, b):
    print(a + b)

# Чому?
# не можна перевикористати
# не можна протестувати
# не можна зберегти результат

#✅ Добре:
def add(a, b):
    return a + b

#---Декомпозиція задачі

# Є список чисел. Треба:
# залишити тільки парні
# піднести їх до квадрату
# порахувати суму

def is_even(n: int) -> bool:
    return n % 2 == 0

def square(n: int) -> int:
    return n * n

def sum_numbers(numbers: list[int]) -> int:
    return sum(numbers)
# Використання:
nums = [1,2,3,4,5,6,7,8,9]


even_nums = [n for n in nums if is_even(n)]
squared = [square(n) for n in even_nums]
result = sum_numbers(squared)

print(result)

#--- *args — змінна кількість аргументів
def add_all(*args):
    total = 0
    for num in args:
        total += num
    return total

add_all(1, 2)
add_all(1, 2, 3, 4, 5)

#--- **kwargs — іменовані аргументи

def print_user(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_user(name="den", age=17, city="Kyiv")
#--- Lambda-функції
square = lambda x: x * x
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, nums))

