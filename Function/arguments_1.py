#area of circle=pi*r*r

def Area(radius,pi=3.14):
    result=pi*radius*radius
    return result

def main():
    #Positional argument
    Output_1=Area(10,12)
    print('Area of circle :',Output_1) #1200 which is wrong

    #First arugument is positional and second one is default
    Output_1=Area(10)
    print('Area of circle :',Output_1)#314.0

#Keyword argument
    Output_2=Area(pi=3,radius=12)
    print('Area of circle :',Output_2)

    #Keyword argument and second is default
    Output_2=Area(radius=12)
    print('Area of circle :',Output_2)

if __name__=="__main__" :
    main()   


# Output:
# Area of circle : 1200
# Area of circle : 314.0
# Area of circle : 432
# Area of circle : 452.15999999999997
















