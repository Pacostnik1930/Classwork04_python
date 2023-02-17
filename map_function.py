# Функция map передает саму функцию

# list1 = [x for x in range(1,20)]
# print (list1)

# list1 = list(map(lambda x : x + 10,list1))
# print(list1)

# Задача:
# С клавиатуры вводится некий набор чисел,в качестве разделителя
# используется пробел.Этот набор чисел будет считан в качестве строки.
# Как превратить list строк в list чисел?

data = '15 156 96 3 5 8 52 5'
# print(data)
# data = data.split()
# print(data)

data = list(map(int, data.split()))
print(data)