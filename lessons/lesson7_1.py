#  for , while

# for variable in objectt iteratsie:
#     deistvie s objectt: 


# ------------------------------------------------

# fruits = ['apple', 'banana', 'orange', 'kiwi']


# for f in fruits:
#     print(f)


# ------------------------------------------------

# nums = [1,2,3,4,5]

# for num in nums:
#     print(num+5)


# ------------------------------------------------


# numbers = 'hello'

# for n in numbers:
#     print(n)

# ------------------------------------------------

#generator of numbers

# for i in range(1, 11): # (start,end,step)
#     print(i)

# ------------------------------------------------

# break and continue

# for i in range(1,11):
#     if i == 5:
#         break    # break - stop iteration
#     print(i)


# for i in range(1,11):
#     if i == 5:
#         continue      #continue - skip one iteration and continue
#     print(i)



# ------------------------------------------------

# #else

# for i in range(1,11):
#     if i == 5:
#         print('five')
# else:
#     print('hello')


# ------------------------------------------------

# nums = [1,2,3,4,5,6,7,8,9,10]
# result = 0

# for num in nums:
#     result += num   #result = result + num

# print(result)
# print(sum(nums))

# ------------------------------------------------

#1
# for i in range(11, 0, -1):
#     print(i)
# print('Start')

# # #2
# for i in range(1, 9, 1):
#     print(f'{i} * 9 = {i * 9}')



# #3
# result = 0
# for i in range(1,101):
#     result += i

# print(result)
    

#4
# nums = '12345'
# result = 0

# for i in nums:
#     result = result + int(i)

# print(result)

# #5
# text = [ "hello","how","are","u"]

# for i in text():
#     print(i)



#6
# 6. Напишите программу, которая подсчитывает количество 
# # гласных букв в строке. 
# words = 'hello world,I LOVE METALLL EYAAAAAAAAA'
# vowels = 'aeiouyAEIOUY'
# count = 0


# # vowels = list('A','E','I','O','U','Y','a','e', 'i', 'o', 'u', 'y')
# words = 'hello world,I LOVE METALLL EYAAAAAAAAA'
# vowels = 'aeiouyAEIOUY'


# for a in words:
#     a.count(vowels)
# print(sum(a))

#7
# result = 1
# for i in range(5, 0, -1):
#     result *= i

# print(result)