import os 

def append(file_01,Content):
    if not os.path.exists(file_01):
        print('File Not exists',file_01)
    else:
       file=open(file_01,'a')

       final=file.write(Content)
       print('Appended Successfull!!')


def main():
    file_01=input("Enter the first file name :")
    Content=input("Enter the Content :")
    append(file_01,Content)

if __name__=='__main__':
    main()    