#open() function-->filename,mode (r,w,a..)

# file_read=open('file.txt','r')
# print(file_read.read())

import os
def Createfile(filename):
    if(os.path.exists(filename)):
        print('File already exists!!')
    else:
        file_create=open(filename,'w')    

    

def main():
    print('Enter the file name you want to Create :')
    file_name=input()

    Createfile(file_name)

if __name__=='__main__':
    main()    




