 # Write a program Which will check the number is greater and equal to and less than and equal to 90.
def check_number(number):
    if(number>=70 and number<=90):
        return number
    
def main():
    size=int(input('Enter the size:'))
    lst=[]
    print("Enter the values:")
    for i in range(size):
        value=int(input())
        lst.append(value)
    print('User List :',lst)
    filter_list=list(filter(check_number,lst))
    print("filtered list is :",filter_list)


if __name__=='__main__':
    main()        
















