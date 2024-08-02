import os

try:
    assert(os.path.exists("file_1.py"))

except:
    print('File Not Exists !!')
finally:
    print('---------The End---------')        