#--- Основні типи Python:

# int — числа без дробу
# float — числа з дробом
# str — рядки
# bool — True / False
# list — список (mutable)
# tuple — кортеж (immutable)
# set — множина
# dict — словник

#--- Приклади:
x = 10            # int
y = 3.14          # float
name = "Денис"    # str
is_active = True  # bool
nums = [1, 2, 3]  # list
coords = (10, 20) # tuple
unique = {1, 2, 3} # set
person = {"name": "Денис", "age": 17} # dict

#--- List Список
books = [1, 2, 3]
books.append[4] #додати 
books.remove[2] #видалити

nums = [1, 2, 3, 4, 5]
squares = [x**2 for x in nums]
print(squares) # [1, 4, 9, 16, 25]

even_squares = [x**2 for x in nums if x % 2 == 0]
print(even_squares) # [4, 16]

#---Словники:
person = {"name": "Денис", "age": 15}
print(person["name"])
person["age"] = 16
person["city"] = "Київ"
