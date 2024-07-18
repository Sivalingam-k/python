# #create a Tuple

# #Homogeneous

# student_id=(123,124,125,126)
ice_cream=('vannila','choco-chips','Blueberry','vannila')

# #Hetrogeneous
mixed_type=(123,'Hello',False,56.78)

# print('Size of Student_id :',len(student_id))
# print('Size of ice_cream :',len(ice_cream))

# #len
# print('Size of mixed_type :',len(mixed_type))

# #usgin index
# print('index of :',mixed_type[len(ice_cream)-1])

# #Using index
# print('index of :',mixed_type[-2])

# #using Slicing

# print('Slicing of :',mixed_type[-3:-1])

# # Size of mixed_type : 4
# # index of : False
# # index of : False
# # Slicing of : ('Hello', False)


# ice_cream=('Vanilla') #str
# print(ice_cream,type(ice_cream))

# ice_cream=('Vanilla',) # put commo for tuple
# print(ice_cream,type(ice_cream))


# #Immutable(Cannot modified)
# mixed_type[0]=True
# print(mixed_type)
# TypeError: 'tuple' object does not support item assignment
#--------------------------------------------------------------------------------------------------------
countmethod=ice_cream.count('vannila')
print('Count Method :',countmethod)

print()

indexmethod=ice_cream.index('vannila')
print('index Method :',indexmethod)


# Count Method : 2

# index Method : 0
#------------------------------------------------------------------------------------------------------
