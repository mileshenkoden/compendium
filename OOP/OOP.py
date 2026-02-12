#---- OOP Об'єктно-орієнтоване програмування

#---Навіщо взагалі ООП

# ООП потрібне, щоб:
# описувати сутності реального світу (User, Order, Task)
# зберігати стан + поведінку разом
# масштабувати код (без хаосу)
# У бекенді 90% логіки — це класи.

#---КЛАС

#--Принцип роботи

# Клас — це шаблон (креслення).
# Обʼєкт — конкретний екземпляр цього шаблону.
# Клас описує:
# які дані є (attributes)
# які дії можна виконати (methods)

class User:
    pass

# class User — оголошення класу
# User — назва класу (CamelCase)
# pass — заглушка (порожній клас)
# Поки що клас нічого не робить.

#--- __init__ і атрибути

#-- Принцип роботи

# __init__ — це конструктор.
# Він викликається кожного разу, коли створюється обʼєкт.
# Він:
# приймає початкові дані
# зберігає їх у обʼєкті

#--Приклад коду
class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

# self — посилання на конкретний обʼєкт
# self.name — атрибут обʼєкта
# name — значення, передане при створенні
user = User("Денис", 17)

#---МЕТОДИ КЛАСУ

#--Принцип роботи

# Метод — це функція, привʼязана до обʼєкта.
# Він працює з атрибутами через self.

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Привіт, мене звати {self.name}"

# greet — метод
# self.name — доступ до даних обʼєкта
# метод викликається через обʼєкт
user = User("Денис", 17)
user.greet()


#--- ІНКАПСУЛЯЦІЯ (публічне vs приватне)

#--Принцип роботи

# Інкапсуляція — приховування внутрішньої логіки.
# У Python це домовленість, а не жорстке правило.

class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def get_balance(self):
        return self._balance

balance = BankAccount(300)
print(balance.get_balance())

# _balance — “protected” (не чіпай напряму)
# доступ через метод
# контроль змін

#--- __repr__

# Python за замовчуванням показує “незрозумілу строчку”.
# __repr__ дозволяє зробити людський вигляд.

class User:
    def __init__(self, name):
        self.name = name

    def rename(self, new_name):
        self.name = new_name

    def greet(self):
        return f"Привіт, мене звати {self.name}"
    
    def __repr__(self):
        return f"User(name={self.name})"
       

user = User("Денис")
print(user.greet())

user.rename("Іван")
print(user.name)

user1 = User("Денис")
user2 = User("Іван")

print(user1.greet())
print(user2.greet())


class Counter:
    count = 0

    def __init__(self):
        self.count += 1

a = Counter()
b = Counter()

print(a.count)
print(b.count)
print(Counter.count)


#---НАСЛІДУВАННЯ

#Базовий клас
class User:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Привіт, мене звати {self.name}"

#Клас-нащадок
class Admin(User):
    def admin_panel(self):
        return "Доступ до адмін-панелі"
#Admin бере все з User

admin = Admin("Денис")

print(admin.greet())
print(admin.admin_panel())

#РОЗШИРЕННЯ, А НЕ ЗАМІНА
class Admin(User):
    def greet(self):
        return f"Я адміністратор {self.name}"

#super() — виклик батьківської логіки
class Admin(User):
    def greet(self):
        base_text = super().greet()
        return base_text + " (адмін)"
admin = Admin("Денис")
print(admin.greet())
#Привіт, мене звати Денис (адмін)


#---ПОЛІМОРФІЗМ

#Базовий приклад
class Animal:
    def speak(self):
        return "Я тварина"
    
#Різна поведінка у нащадків
class Dog(Animal):
    def speak(self):
        return "Гав"

class Cat(Animal):
    def speak(self):
        return "Мяу"

animals = [Dog(), Cat(), Animal()]

for animal in animals:
    print(animal.speak())

#--Поліморфізм через super()
class LoggedDog(Dog):
    def speak(self):
        base = super().speak()
        return base + " (з логом)"
dog = LoggedDog()
print(dog.speak())

#---КОМПОЗИЦІЯ vs НАСЛІДУВАННЯ

#--НАСЛІДУВАННЯ (is a)
class Engine:
    def start(self):
        return "Двигун запущено"

class Car(Engine):
    pass

car = Car()
print(car.start())

#--КОМПОЗИЦІЯ (has a)
class Engine:
    def start(self):
        return "Двигун запущено"

class ElectricEngine:
    def start(self):
        return "Електродвигун запущено"

class Car:
    def __init__(self, engine):
        self.engine = engine

car1 = Car(Engine())
car2 = Car(ElectricEngine())

print(car1.engine.start())
print(car2.engine.start())






