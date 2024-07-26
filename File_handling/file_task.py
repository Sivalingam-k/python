import os
import filecmp 
def delete_content(delete_file):
    if not os.path.exists(delete_file):
        print('File Not exists',delete_file)
    else:
        del_file=os.remove(delete_file)
        print({del_file},'File Deleted Successfully!!')    

def copy_content(exist_file, new_file):
    if not os.path.exists(exist_file):
        print(f'File not exists: {exist_file}')
    else:
        file_01 = open(exist_file, 'r')
        file_val = file_01.read()
       
        file_02 = open(new_file, 'w')
        file_02.write(file_val)
        print(f'Success ->Copying file from{exist_file} to {new_file}')
        compare=filecmp.cmp(exist_file,new_file)
        if compare==True:
            print('Success !! The files are Same..')
        else:
            print('Failure !! The files are Different ...')       
 
def main():
    exist_file = input('Enter the name of the exist_file : ')
    new_file = input('Enter the name of the new_file  : ')
    copy_content(exist_file, new_file)
    delete_file=input("Enter the file name to delete :")
    delete_content(delete_file)
 
if __name__ == "__main__":
    main()
