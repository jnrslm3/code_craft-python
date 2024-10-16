# while

# while condition:
#     block of code work while condition True





# ------------------------------------------------



# num = 5
# count = 0

# while count <= 10:
#     count +=1
#     print(count)


# ------------------------------------------------\


# password = '12345'

# user_input = input('enter a password: ')
# while user_input != password:
#     print('incorrect password, try again')
#     user_input = input('enter a password')



# ------------------------------------------------\


# password = '12345'

# user_input = input('enter a password: ')
# while True:
#     if user_input == password:
#         print('password is correct')
#         break
#     else:
#         print('incorrect password, try again')
#         user_input = input('enter a password: ')


# ------------------------------------------------\

# password = '12345'
# flag = True

# user_input = input('enter a password: ')
# while flag:
#     if user_input == password:
#         print('password is correct')
#         flag = False
#     else:
#         print('incorrect password, try again')
#         user_input = input('enter a password: ')

# ------------------------------------------------\
# continue

# count = 0 

# while count < 10:
#     count += 1
#     if count == 5:
#         continue
#     print(count)

# ------------------------------------------------\
# #1
# num = 0
# count = 0


# user_input = int(input('enter num: '))
# while user_input != num:
#     count += user_input
#     print(f'try again, also sum of ur num {count}' )
#     user_input = int(input('enter num: '))



#2

# user_input = int(input('enter ur num: '))

# while user_input != 0:
#     print(user_input)
#     user_input = user_input - 1
    




# #3
# count = 0
# total = 0


# num = int(input('enter num: '))
# while num != 0:
#     total += num
#     count += 1
#     print( total / count)
#     if count >0:
#         num = int(input('enter num: '))
        


 


# 4

# password = '1233'
# count = 1


# user_input = input('enter a password: ')

# while user_input != password:
#     print('password is incorrect, try again')
#     user_input = input('enter a password: ')
#     count += 1
#     if count == 3:
#         print('u reach a limit!')
#         break