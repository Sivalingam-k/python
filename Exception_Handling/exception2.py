import datetime

try:
    today=datetime.date.today()
    year=today.year
    # num1=int(input("Enter NUmber 1 :"))
    # num2=int(input("Entert nNumber 2: "))
    # result=num1/num2
    # print(result)
    items=["Bread","Butter","Jam","Cheese"]
   # items[len(items)]="spread"
    # #Assertion error:
    # num1=int(input("Enter NUmber 1 :"))
    # assert num1%2==0
    # print(num1, " is Even")



except ZeroDivisionError:
    print("Error: Denominator Cannot be Zero") 
except ValueError:
    print("Only Numbers are Allowed!!")  
except IndexError:
    print("Kindly use insert or append method to insert!")  
except AssertionError:
    print(num1, " is Odd or Not Even Number") 
finally :
    print('--->>>>> Program is Over <<<<<----')    

yob=int(input("Enter Your Year of Birth :"))
age=year-yob

if(age<18):
    raise Exception(f'Age should greater than 18 but your age is {age}')
print(age)    