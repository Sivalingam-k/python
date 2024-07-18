# #Creating a list
# #Homogenoeous
# course=['python','Java','Php']
# rollno=[123,234,345]
# print("Homogenoeous :",course)
# print("Homogenoeous :",rollno)
# #Hetrogenous

# student=['siva',123,True,67.78]
# print("Hetrogenous :",student)

# #Finding length
# print('length of hetrogenous student array :',len(student))

# #Access Data On Positive Index

# print('Access of hetrogenous student array :',student[1])
# print('Access of hetrogenous student array :',student[2])

# #Access Data On Negative Index
# print('Access of hetrogenous student array :',student[-3])
# print('Access of hetrogenous student array :',student[-1])
# print('Access of hetrogenous student array :',student[-2])

# #Slicing : [start:stop(excluded)] from start index to before stop index
# #['Siva', 123,True] using Positive index
# print('Slicing',student[1:3])

# #['Siva', 123,True] using negative index

# print('Slicing',student[-4:-1])

#==============================================================================================================

#Mutable(can change,add and delete)

fruits=['Mango','Banana','Grapes','WaterMelon']

fruits[1]='Kiwi'
print ('Using Index Replacing banana with Kiwi',fruits)

del fruits[3]
print('Removing Watermelon',fruits)



fruits[1:3]=['banana','orange']
print(fruits)
#['Mango', 'banana', 'orange']




















