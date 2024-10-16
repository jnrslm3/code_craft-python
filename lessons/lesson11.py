# function

# ------------------------------------------------

# def func_name():
#     #code

# def name():
#     a = input('enter ur name: ')
#     print(a)
# name()

# ------------------------------------------------

# def hello(name,age,male): # argument
#     print(f'Hello {name},{age},{sex}')

# hello('Nurislam',16,'M')

# ------------------------------------------------

# default argument

# def hello(name,age,male = None): # argument
#     print(f'Hello {name}, {male}')

# hello('Nurislam',16)

# ------------------------------------------------

#positional and named arguments

# def hello(name,age,male): # argument
#     print(f'Hello {name}, {male}')

# hello('Nurislam',16)

# ------------------------------------------------

# def math(a,b):
#     print(f'area of rectangle is {a * b}')

# math(5,7)

# ------------------------------------------------

# args and kwargs

# def nums(*args, **kwargs): 
#     print(args)     # args = arguments, (for unlimited positioned arguments)
#     print(kwargs)   # kwargs = key words arguments, (for unlimited named arguments)


# nums(1,2,3,4,5,6,7,8,9,10, name='Alikhan', age=12. male='w')
# ------------------------------------------------

# def hello():
#     n = 5+9
#     return n # operator vozvrasheniye from function

# print(hello())

# ------------------------------------------------


# oblast vidimosty 


# def hello(name):
#     print(f'hello {name}')

# hello('Alikhan')


# ------------------------------------------------

# lambda function(anonym function)

# num = lambda a, b: a + b # arguments
# print(num(5,6))

# ------------------------------------------------

#vlojennye function

# def hello(name):
#     def inner():
#         print(f'hello {name}')
#     inner() # recall vlojennye function

# hello('Alikhan')

# ------------------------------------------------

#zamykanie 

# def hello(msg):
#     def n():
#         print(msg)
#     return n

# g = hello('Hey bro')
# g()

# ------------------------------------------------

# rekursia

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(int(input('enter ur num to factorial it: '))))




