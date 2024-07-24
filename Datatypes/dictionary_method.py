watch_details={
    'Titan':8000,
    'Fastrack':5000,
    'Omega':9000,
    'Titan':82000
}

#Keys() ==>Returns a list containing the dictionary keys.

key_method=watch_details.keys()
print('Key Method :',key_method)
#Key Method : dict_keys(['Titan', 'Fastrack', 'Omega'])

#value method

value_method=watch_details.values()
print('value Method :',value_method)
#value Method : dict_values([82000, 5000, 9000])

#get method

get_method=watch_details.get('Titan')
print('get Method :',get_method)
#get Method : 82000

#Item method ==>dictionary to tuple
Item_method=watch_details.items()
print('Item Method :',Item_method)
#Item Method : dict_items([('Titan', 82000), ('Fastrack', 5000), ('Omega', 9000)])


#Update method==> insert an item to the dictionary

watch_details.update({'Noise':12000})
print('Update Method :',watch_details)
# Update Method : {'Titan': 82000, 'Fastrack': 5000, 'Omega': 9000, 'Noise': 12000}


#pop Method
watch_details.pop("Titan")
print('pop Method :',watch_details)
#=================================================================================================================









