watch_details={
    'Titan':8000,
    'Fastrack':5000,
    'Omega':9000,
    'Titan':12900
}
print('Watch Available :',watch_details)
print(len(watch_details))
print(type(watch_details))
# 3
# <class 'dict'>

print('Using Key',watch_details['Titan'])

#if you make a duplicate of  the key.Then ,it will take the latest duplicate key's value.so the key should be unique.

watch_details={
    'Titan':8000,
    'Fastrack':5000,
    'Omega':9000,
    'Cartier':82000
}
print('Watch Available :',watch_details)
print(len(watch_details))
print(type(watch_details))
# 3
# <class 'dict'>

print('Using Key',watch_details['Titan'])
print('Using Key',watch_details['Cartier'])

# Watch Available : {'Titan': 12900, 'Fastrack': 5000, 'Omega': 9000}
# 3
# <class 'dict'>
# Using Key 12900
# Watch Available : {'Titan': 8000, 'Fastrack': 5000, 'Omega': 9000, 'Cartier': 82000}
# 4
# <class 'dict'>
# Using Key 8000
# Using Key 82000

#------------------------------------------------Modify------------------------------------------

watch_details["Omega"]=4000

print("Modified Data :",watch_details)

#------------------------------------------------Adding------------------------------------------
watch_details["IWC"]=7000

print("Adding Data :",watch_details)


#create a  food item dictionary
food_item={
    'chappthi':20000,
    'vada':42,
    'Dosa':88888,
    'Tea':300
}
#------------------------------------------------Modify------------------------------------------

food_item["vada"]=60000

print("Modified Data :",food_item)

#------------------------------------------------Adding------------------------------------------
food_item["Biriyani"]=100

print("Adding Data :",food_item)

