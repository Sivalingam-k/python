#==================================RANGE FUNCTION====================================================

for i in range(5):
    print(i) # It will print 0 to 4 

for i in range(2,11):
    print(i) # It will print 2 to 10 

for i in range(2,11,2):
    print(i) # It will print 2,4,6,8,10

for i in range(2,11/2,2):
    print(i) # It will print error because of 5.5

    for i in range(2,int(11/2),2):
    print(i) # It will print 2,4.


#int(11/2) ==>5
#11/2 ==>5.5