#unchangeable types of data
# str
# int
# float
# bool
# tuple
# frozenset

# changeable types of data
# list
# set
# dict



# bytes



# ------------------------------------------

# coordinates = (10, 20, 'xdv', '213') #tuple

# # print(coordinates.index(10))
# # print(coordinates.count('213'))
# h = coordinates[5].append(122)

# print(coordinates)


# ------------------------------------------

# #set and methods

# numbers = {'hello', 'we', 'werr', 'we'}

# # numbers.clear()                                #clear 
# # numbers.add('xdv')                             #add element 
# # numbers.remove('we')                           #remove element
# # numbers.discard('we')                          #delete element and not argue
# # numbers.update(['xdv', 'werr'])                #update set
# # numbers.pop()                                  #delete random element
# # numbers.difference_update(['hello', 'we'])     #delete everything that written in this list


# print(numbers)


# ------------------------------------------

#EXERCISES


#1
# list1 = [0,1,2,3,4,5,6,7]

# print(list1[0:8:2])

# #2
# list2 = [10,20,30]

# print(sum(list2)/len(list2))

#3
# tuple1 = (1,2,3)
# tuple2 = (4,5,6)

# text = tuple1 + tuple2
# print(text)

# # 4
# list1 = (10, 20, 30, 40)
# print(list1[::-1])

# # #5

# list1 = set([10, 20, 30, 40])
# list2 = set([10, 20])
# print(list1-list2)



# # #6
list1 = [3, 1, 4]
list2 = [5, 2, 6]

list3 = list1 + list2

print(list3)
list3.sort(reverse=True)


print(list3)

#7

# list1 =  {1, 2, 3, 4}
# list2 =  {3, 4, 5, 6}
# print(list1-list2)

# #8
# list1 = {1, 2, 3, 4}
# list2 = {3, 4, 5, 6}

# print(bool(list1 == list2))