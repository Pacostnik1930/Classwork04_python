# Функция filter на вход принимает 2 значения(сама функция и объект)
# Будет возвращать только те элементы объекта для которых вызов функции,
# которую мы передали вернули значение True

# list1 = [15,65,9,36,175]
# result = list(filter(lambda x: x % 10 == 5,list1))
# print(result)


list1 = [1,2,3,5,8,15,23,38]
result = map(int,list1)
print(result)
result = filter(lambda x : x % 2 == 0,result)
print(result)

result = list(map(lambda x: (x**2),result))
print(result)