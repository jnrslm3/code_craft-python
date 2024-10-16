# decorators

# def my_decorator(func):
#     def wrapper():
#         print('smth is happening before the function is called.')
#         func()
#         print('smth is happening after the function is called')
#     return wrapper

# @my_decorator
# def say_hello():
#     print('Hello')

# say_hello()



# ------------------------------------------------

# decoration with arguments


# def my_decorator(func):
#     def wrapper(*args,**kwargs):
#         print('smth is happening before the function is called')
#         print(func(*args))
#         print('scare of numbers')
#     return wrapper

# @my_decorator
# def say_hello(num, num2):
#     return num + num2

# say_hello(5,5)

# ------------------------------------------------

# amount of decorators

# def my_decorator1(func):
#     def wrapper():
#         print('decorator1')
#         func()
#     return wrapper

# def my_decorator2(func):
#     def wrapper():
#         print('decorator2')
#         func()
#     return wrapper


# @my_decorator2
# @my_decorator1
# def say_hello():
#     print('hello')

# say_hello()

# ------------------------------------------------
# decorator with arguments u seba



# def repeat(num):
#     def decorator_repeat(func):
#         def wrapper(*args):
#             for i in range(num):
#                 func(*args)
#         return wrapper
#     return decorator_repeat

# @repeat(n)
# def say_hello(name):
#     print(f'hello {name}')

# say_hello('alikhan')


# ------------------------------------------------
from random import randint


#1
# def my_decorator(func):
#     def wrapper():
#         if 10 < func():
#             print("Result is greater than 10" )
#         else:
#             print("Result is not greater than 10")
#     return wrapper


# @my_decorator
# def check():
#     num = randint(1,20)
#     print(num)
#     return num

# check()


# #2
def my_decor(func):
    def wrapper():
        try:
            
        except:
            print('An exception occurred!')
    return wrapper

# @my_decorator
def number():
    num = randint(1,10)
    print(num)
    return num

number()


#3
# def my_decor(func):
#     def wrapper():
#         if func() % 2 != 0:
#             print('result is odd number')
#         else:
#             print('result is even number')
#     return wrapper


# @my_decor
# def check():
#     num = randint(1,20)
#     print(num)
#     return num

# check()