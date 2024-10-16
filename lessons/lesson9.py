# Working with files

# ------------------------------------------------

# file = open('test.txt', 'r') # r - read the file 
# content = file.read() # read whole content of file
# # content2 = file.readlines() #readlines - count all strings in the list 
# # print(content.strip()) # remove spaces in the begging and end 
# # print(content2)
# # content = file.readline() # readline() - count one string
# print(content)
# # for line in file:
# #     print(line.strip())
# file.close() # close the file 


# ------------------------------------------------
# print('hello  \n  world') # return
# print('hello  \t  world') # tab
# ------------------------------------------------

#w

# file = open('test.txt', 'w', ) # w - write, note in the file, create new file if the file don't exist
# file.write('John Smith ')  # write - rewrite the file
# file.writelines(['\nHello', '\nWorld']) # add in the file 
# file.close()

# ------------------------------------------------

#a 
# file = open('test.txt', 'a') # a - append, add in the file
# file.write('\nHello World') # write - add in the file
# file.writelines(['\nHello', '\nWorld']) # add in the file 
# file.close()


# ------------------------------------------------

# #with
# with open('test.txt', 'r') as file:
#     content = file.read()
#     print(content)

# ------------------------------------------------

# positions and indicator

# with open('test.txt' , 'r') as file:
#     print(file.tell()) # tell - show position of indicator
#     file.seek(8) # replace indicator for 8 bits
#     print(file.read()) # read with 8 position

# ------------------------------------------------

# # r+ , a+ , w+
# words = '\nHello world'
# with open('test.txt' , 'r+') as file:
#     file.write(words) 
#     print(file.read())

# ------------------------------------------------
# Exercises

# # #1
# with open('test.txt', 'r+') as file:
#     content = file 
#     for i in content :
#         i.split()
#         len(i)
#         print(max(content, key=len))
    

#2 
# with open('test.txt', 'a+') as file:
#     file.write(input('enter ur word: '))
#     file.seek(0)
#     print(file.read())

# #3
# with open(input('Have you ever been into Moscow, Paris, or Budapest: ')+'.txt', 'a+') as file:
#     file.write(input('write ur experience and feedback: '))