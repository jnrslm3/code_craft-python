#DICTIONARY
#                    key : value
# students_exams = {'Ivanov': 60, 'Petrov': 78, 'Sidorov': 85}

#methods ------------------------------------

# print(students_exams.keys())                  # show all keys
# print(students_exams.values())                # show all values
# print(students_exams.items())                 # show all keys and values
# print(students_exams.get('Ivanov'))           # show value by key
# print(students_exams.pop('Ivanov'))           # delete key and value
# # print(students_exams.popitem())             # delete last key and value
# students_exams.update({'Ivanov2':90})         # add key and value
# print(students_exams.clear)                   # clear dictionary
# # print(students_exams['Petrov'])             # give value by key
# students_exams['Petrov'] = 90                 # change value by key
# # del students_exams['Ivanov']                       # delete key and value
# students_exams.setdefault('Ivanov', 80)              # add key and value, if key isn't in dictionary
# students_exams.fromkeys(['Ivanov2','Petrov2'], 80)   # create new key with value
# students_exams.copy()                                #copy dictionary

# print(students_exams)


# ------------------------------------------------

#EXERCISES

# #1
# students = {'John': 85,'Emily': 92,'Michael': 78,'Sophia': 95,'David': 87}

# total = sum(students.values())
# average_score = total / len(students)
# print(average_score)

# # #2
# workers = {"John": 25, "Alice": 30, "Bob": 22}
# a = max(workers.values())
# print(a)

# #3
# gpa = {"John": [5, 4, 3], "Alice": [2, 4, 5], "Bob": [4, 4, 4]}

# average = sum(gpa.values())
# total = average/len(students)

# #4
# fruits =  {"apple": 2, "banana": 4, "cherry": 3}



# ------------------------------------------------


