# def sum_all(*args):
#     count=0
#     for i in args:
#         count+=i
#     return count

# output=sum_all(1,2,3,4,5)    
# print('Addition of all :',output)    

def StaffDetails(**kwarg):
    for key,value in kwarg.items():
        print(f'{key} is {value}')


def main():
    changepond={'Name':'gokul',
    'Age':21,
    'Mobile':5678903
    } 
    StaffDetails(**changepond)   
# def main(*args):
#     for i in args:
#         print(i)
#         for j in i:
#             print(j)
  
# changepond=main(['gokul','Ajith','suresh','sandeep''vijay'])

if __name__=='__main__':
    main()