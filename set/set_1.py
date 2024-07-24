#Creating a set

staff_id={123,124,125,126} #same Datatype
mixed_type={'Shubham',25,124,True,124} #Mixed  Datatype

print('Set :',mixed_type)
print('Length :',len(mixed_type))#4 because set dont allow duplicate

s1={True,0,1,False}
print(s1)

#True->1
#False -> 0
s1={True,1}
print(s1)

#Task Iterating using for loop

for mixed in mixed_type:
    print(mixed)


#     Set : {'Shubham', 124, 25, True}
# Length : 4
# {0, True}
# {True}
# Shubham
# 124
# 25
# True