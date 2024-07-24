#Using listcomprehension creating a list of square numbers

#new_list=[expression for member in iterable]
#new_list=[expression for member in iterable if(optional)]


new_list=[i for i in range(1,11)]
print('List Comprehension :',new_list)

new_list=[i for i in range(1,11) if(i%2==0)]
print('List Comprehension of even numbers :',new_list)

name="Siva"
vowels="aeiou"
new_list=[i for i in name if (i in vowels)]
print('List Comprehension of Vowels in name :',new_list)
