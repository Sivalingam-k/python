from functools import reduce 
def checkSplletter(checkSplChar):
    special_Char = ['!','@','#','$','%','^','&','*','(',')','-','_','/','?','~',',','<','>','.',':',';','\'','\"','+','=','[',']','{','}']
    for ch in checkSplChar:
        if ch in special_Char:
            return False
        else:
            continue
    return checkSplChar    

def remove_chr(values):
    var = ""
    for i in values:
        if "0" <= i <= "9":
            var=var+i
    return int(var)
 
def main():
    # size=int(input('Enter the size:'))
    # lst=[]
    # print("Enter the values:")
    # for i in range(size):
    #     value=int(input())
    #     lst.append(value)
    # print('User List :',lst) #getting Users List

    # #Mapping
    # map_list=list(map(lambda num:num**3,lst)) #[1,2,3,4,5]
    # print("Map list is :",map_list)
    # print()

    # #1->num1,2->num2=>3
    # #3-num1,3->num2 =>6
    # #6-num1,4->num2 ==>10
    # #10->num1,5-->num2==>15

    # reduce_list =reduce((lambda num1,num2:num1+num2),map_list)
    # print('Reduce List :',reduce_list)


    # print('Reduce Value ',reduce_list) TASK
    course = ['','Python','java',',,','angul:ar','php']

    filter_list = list(filter(checkSplletter,course))
    print('Filter List : ',filter_list)

    product_id = ['HEM-234','HEM-123','HEM-566']   #[234,123,566]
    filtered_id = list(map(lambda val: int(val[4:7]), product_id))
    print(filtered_id)
    product_ids = ['HEM-234', 'HEM-123', 'HEM-566'] 
    number_ids = list(map(lambda x: int(x.split('-')[1]), product_ids)) 
    print(number_ids)

    

    
    Only_number= list(map(remove_chr,product_id))
    print(Only_number)

#Task 3
#sort a dictionary by value in python (lambda function)
detail=[
{'name':'shreya','age':15},
{'name':'pratiksha','age':13},
{'name':'prerna','age':15}
 
]
sorted_list = sorted( detail, key=lambda val: val['age'] )
print(sorted_list)
    

if __name__=='__main__':
    main()      