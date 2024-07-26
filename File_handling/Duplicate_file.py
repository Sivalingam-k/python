import os
import filecmp
def duplicate(file_01,file_02):
    if not os.path.exists(file_01):
        print('File Not Exits')
    if not os.path.exists(file_02):
        print('File Not Exits')    
    else:
        compare=filecmp.cmp(file_01,file_02)
        if compare==True:
            os.remove(file_02)
            print('Duplicate File is removed !!')
        else:
            print('Different Content!! No Duplicate')    

def main():
    file_01=input("Enter First File name :")
    file_02=input("Enter Second File Name :")

    duplicate(file_01,file_02)



if __name__=='__main__':
    main()    