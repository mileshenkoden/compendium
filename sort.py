#----- map, filter, sorted

#--- map
#- map(function, iterable)

nums = [1, 1.5, 3]
result = list(map(lambda x: x * x, nums))
print(result)
# це все одно що [x * x for x in nums]

#--- filter

#- filter(function, iterable)
#-- ➡️ залишає елементи, для яких функція повертає True
filter(is_even, nums)
# те саме що і [x for x in nums if is_even(x)]


#--- sorted

#- sorted(iterable, key=..., reverse=False)

users = [{"name": "A", "age": 20}, {"name": "B", "age": 0}]
sort_user = sorted(users, key=lambda u: u["age"])
print(sort_user)

#- key — функція, яка каже по чому сортувати