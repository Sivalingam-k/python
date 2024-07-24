def subject():
    dict_mark={}
    for i in range(1):
        dict_mark["python"]=int(input('Enter The python mark :'))
        dict_mark["Java"]=int(input('Enter The Java mark :'))
        dict_mark["react"]=int(input('Enter The react mark :'))
        dict_mark["dotnet"]=int(input('Enter The net mark :'))  

    return dict_mark
def main():
    marks=subject()
    total=0
    for i in marks:
        total= total+marks[i]
    print(total)
    if(total>350):
        print('Excellent!! You are Scored A Grade')  
    elif(total>300):
        print('Congrats!! You are Score B Grade')  
    elif(total>275):
        print('Good!! You are Score C Grade')  
    elif(total>250):
        print('Hmm!! You are Score D Grade') 
    else:
        print('Scored Low mark.. Try lot..')       


   
if __name__=='__main__':
    main()      