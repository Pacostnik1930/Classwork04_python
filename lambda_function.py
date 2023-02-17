# def f (x):
#     return x*x
# #print(f(5))
# a = f
# #print(type(f))
# print(a(5)) 
# print(f(5))

# Создание калькуцлятора

# def calc1(a):
#     return a + a

# def calk2(a):
#     return a * a

# def math(op,x):
#     print(op(x))

# math(calc1,5)    


# def calc1(a,b):
#     return a + b

# def calc2(a,b):
#     return a * b

# def math(op,x,y):
#     print(op(x,y))

# math(calc2,5,45)    

# Создание лямбда функции /  Сокращение кода

# def calc1(a,b):
#     return a + b

# def calc2(a,b):
#     return a * b

# def math(op,x,y):
#     print(op(x,y))

# calc1 = lambda a,b : a + b

# math(lambda a,b:a+b,5,45)    

# Задача:
# В списке хранятся числа.Нужно выбрать только четные и составить список пар(число,квадрат числа)  
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2,4),(8,64),(38,1444)]

# list1 = [1,2,3,5,8,15,23,38]

# result = list()

# for i in list1:
#     if i % 2 == 0:
#         result.append((i,i**2))
# print(result)


# Решение задачи через лямбду

def select(f,col):
    return [f(x) for x in col]

def where(f,col):
    return[x for x in col if f(x)]

list1 = [1,2,3,5,8,15,23,38]
result = select(int,list1)
print(result)
result = where(lambda x : x % 2 == 0,result)
print(result)

result = list(select(lambda x: (x**2),result))
print(result)

# Решение через функцию map



def where(f,col):
    return[x for x in col if f(x)]

list1 = [1,2,3,5,8,15,23,38]
result = map(int,list1)
print(result)
result = where(lambda x : x % 2 == 0,result)
print(result)

result = list(map(lambda x: (x**2),result))
print(result)