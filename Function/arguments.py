def function_name(value_01,value_02):
    print('Inside addition')
    print('Value 1 :',value_01)
    print('Value 2 :',value_02)
    add=value_01+value_02
    sub=value_01-value_02
    return add,sub
  
if __name__=="__main__": #Main function
    function_name(10,20)

    