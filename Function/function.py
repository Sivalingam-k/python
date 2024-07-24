# def function_name():
#     a=10
#     b=20
#     c=a+b
#     print('Addition: A+B ',c)
# function_name()

# # one parameter one argument
# def function_name(value_01):
#   print(value_01)
# function_name(10)

#Return(used to exit from the function and go back to the function caller and return the specified value
# or data item)

def function_name(value_01,value_02):
    print('Inside addition')
    print('Value 1 :',value_01)
    print('Value 2 :',value_02)
    add=value_01+value_02
    sub=value_01-value_02
    return add,sub
  
add,sub=function_name(10,2)

print('addition is ',add)
print('subtraction is',sub)

# Output:
# Inside addition
# Value 1 : 10
# Value 2 : 2
# addition is  12
# subtraction is 8