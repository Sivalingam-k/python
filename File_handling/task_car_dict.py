def make_car(manufacturer,model,**kwargs):
    print(manufacturer)
    print(model)
    for key,value in kwargs.items():
        print( f'{key} is {value}')
def main():
 
    make_car('Ford' , 'outback' ,color = 'Blue' , rate=1000)
if __name__=="__main__":
    main()