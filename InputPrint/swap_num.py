num1=int(input("Enter First Number "))
num2=int(input("Enter Second Number "))
print("Original Variables are:",num1,num2)
print("Swap Numbers Using  Temporary Variable ")
temp=num1
num1=num2
num2=temp
print("swap 1 Variables are:",num1,num2)
#num1=20 num2=10

print("Swap Numbers Using  + and - Operator ")
num1=num1+num2 #20+10=30
num2=num1-num2 #30-10=20
num1=num1-num2 #30-20=10

print("swap 2 nd time Variables are:",num1,num2)

print("Swap Numbers Using  * and / Operator ")
num1=num1*num2 #20*10=200
num2=num1/num2 #200/10=20
num1=num1/num2 #200/20=10

print("swap 3 rd time  Variables are:",num1,num2)