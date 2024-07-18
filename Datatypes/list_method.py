# menu_card=['panner','Dal','Rice']

# #Append()--> Adds an element at the end of the list

# menu_card.append('Kofta')
# print('After Using Append : ',menu_card)
# # After Using Append :  ['panner', 'Dal', 'Rice', 'Kofta']

# #'dal','Biriyani'
# #Extend()--> Add the elments of a list(or iterable) to the end of list

# menu_card.extend(['Dal','Biriyani']) # always in list(array)
# print('Using extend method :',menu_card)


# # Using extend method : ['panner', 'Dal', 'Rice', 'Kofta', 'Dal', 'Biriyani']

# #-----------------------------------------------------------------------------------------------------

# #insert  --> Adds an element ata the specified position

# menu_card.insert(2,'Veg-Biriyani')
# print('Using Insert Method :',menu_card)
# #Using Insert Method : ['panner', 'Veg-Biriyani', 'Dal', 'Rice', 'Kofta', 'Dal', 'Biriyani']

# #Remove() Method---> will remove specified value

# menu_card.remove('Dal')
# print('Using Remove Method :',menu_card)

# #Using Remove Method : ['panner', 'Veg-Biriyani', 'Rice', 'Kofta', 'Dal', 'Biriyani']


# #Pop() --> removes element of specified position
# menu_card.pop(2)
# print('Using Pop Method :',menu_card)

# # Using Pop Method : ['panner', 'Veg-Biriyani', 'Kofta', 'Dal', 'Biriyani']

# #------------------------------------------------------------------------------------------------------

menu_card=['panner','Dal','Rice']

#index_Method

index_method=menu_card.index('Rice')
print('It will Give Position :',index_method)

#Sort method

menu_card.sort()
#menu_card.sort(reverse=True)
print('Using Sort Method :',menu_card)
















