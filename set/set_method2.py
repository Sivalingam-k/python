company={'Infosys','ICICI bank','TCS','Bajaj'}
add_company={'SBI','TATA consultancy','Infosys','TCS'}

#union method

union_method=company.union(add_company)
print('Union method will return all the Element :',union_method)

#Union method will return all the Element : {'SBI', 'Infosys', 'TCS', 'Bajaj', 'TATA consultancy', 'ICICI bank'}

#union method using operator

union_method=company | add_company
print('Union method using oprator :',union_method)

#Union method using oprator : {'Bajaj', 'TCS', 'SBI', 'TATA consultancy', 'Infosys', 'ICICI bank'}

intersection_method=company.intersection(add_company)
print('Intersection method will return common elements :',intersection_method)

#Intersection method will return common elements : {'Infosys', 'TCS'}

#Difference Method

Difference_method=company.difference(add_company)
print('Difference method will return non-commam elements from comapny only:',Difference_method)
#Difference method will return common elements : {'Bajaj', 'ICICI bank'}


#symentric_method()

symm_difference = company.symmetric_difference(add_company)
print('symm_difference will return non-commam elements from both comapny and add_company: ',symm_difference)

#symm_difference:  {'TATA consultancy', 'ICICI bank', 'Bajaj', 'SBI'}

























