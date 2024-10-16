# if else elif ( Операторы условия)

# if условие :
#            выполенение кода если условие True
# if 'hello'=='Hello':
#   print ('условие True')


# ------------------------------------------------



# password = input('Enter password: ')

# if password == 'qwerty123':            # if - если
#     print( 'Пароль верный' )
# else:                                  # else - иначе
#     print ('Пароль не верный' )



# ------------------------------------------------



# if 7>8:
#     print('condition if is correct')
# elif 5>4:
#     print('condition elif is correct')
# else:
#     print('nothing is correct')



# ------------------------------------------------


# if 5 == 5:
#     if 5>4:
#         print('hello')
#     else:
#         print('ne hello')
# else:
#     print('hz')



# ------------------------------------------------

## operators if 

#        and


# if 1>9 and 5>3: # and - and
#     print('condition true')
# else:
#     print('condition false')



# ------------------------------------------------

#        or


# if 1>9 or 5>3: # or - или , хотябы одно улсовие должно быть верно
#     print ('условие True')
# else:
#     print("условие False')


# ------------------------------------------------


#         in

# name = ('er', 'wer')

# if 'er' in 'Nightmer' : #in - в(внутри)
#     print ('yes')
# else:
#     print( 'no')



# ------------------------------------------------


# not True == False
# not False == True
# not


# name = 'Hello'
# if 'e' not in name: # not - не
#     print( 'yes')
# else:
#     print( 'no')


# if 5 != 5:
#     print( 'yes')
# else:
#     print( 'no')


    
# if 5 == 5:
#     print( 'yes')
# else:
#     print( 'no')


# ------------------------------------------------

#homework 

# #1
# user_num = int(input('enter ur num: '))

# if user_num % 2 == 0 and user_num % 3 == 0:
#     print('ur num is even and can divided by 3')
# else:
#     print('ur num is even or odd but can not divided by 3')


# #2
# user_age = int(input('enter ur age: '))

# if user_age <13 :
#     print('ur kid')
# elif user_age == 13 or user_age < 17:
#     print('ur teenager')
# else:
#     print('ur adult')

# #3
# user_birth_year = int(input('enter a year when you was born : '))

# if user_birth_year % 4 == 0 and user_birth_year % 100 != 0 or user_birth_year % 400 == 0 :
#     print('год високосный')
# else:
#     print('год не високосный')

# #4
# a = int(input('enter ur first num: '))
# b = int(input('enter ur second num: '))
# c = int(input('enter ur third num: '))

# all_nums = [a , b , c]
# all_nums.sort()

# print(all_nums)

# #5
# lst = input("Введите элементы списка через пробел: ").split()
# if len(lst) == len(set(lst)):
#     print("Все элементы уникальны.")
# else:
#     print("Есть повторяющиеся элементы.")



#6

# user_age18 = int(input('enter ur age: '))
# user_license =  input('do you have driving license: (yes/no) ').strip().lower()

# if user_age18 >= 18 and user_license ==  'yes':
#     print('you can drive a car')
# else:
#     print('you can not drive a car')


# ------------------------------------------------


# import math

# def solve_quadratic(a, b, c):
#     # Calculate the discriminant
#     discriminant = b**2 - 4*a*c

#     # Check the nature of the discriminant
#     if discriminant > 0:
#         # Two real and distinct roots
#         root1 = (-b + math.sqrt(discriminant)) / (2 * a)
#         root2 = (-b - math.sqrt(discriminant)) / (2 * a)
#         return f"The equation has two real roots: {root1} and {root2}"
#     elif discriminant == 0:
#         # One real root
#         root = -b / (2 * a)
#         return f"The equation has one real root: {root}"
#     else:
#         # Complex roots
#         real_part = -b / (2 * a)
#         imaginary_part = math.sqrt(-discriminant) / (2 * a)
#         return f"The equation has two complex roots: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i"

# # Input coefficients
# a = float(input("Enter the coefficient a: "))
# b = float(input("Enter the coefficient b: "))
# c = float(input("Enter the coefficient c: "))

# # Solve the quadratic equation
# result = solve_quadratic(a, b, c)
# print(result)


