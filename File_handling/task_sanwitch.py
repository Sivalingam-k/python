def order_sandwich(*items):
    print("You have ordered the following items:")
    for item in items:
        print(item)
 
def main():
    try:
        order=[]
        num_of_items=int(input("Enter number of items : "))
        for i in range(0,num_of_items):
            order.append(input())
            order_sandwich(*order)
    except ValueError:
        print('Only Integers are allowed!!')
    finally :
        print('Programs End!')    

if __name__ == "__main__":
    main()