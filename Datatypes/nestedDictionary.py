#NestedDictionary

users={
    'kastubag':{
        'firstname':'kasturi',
        'lastname':'Chaware',
        'Location':'pune'
    },
    'shrebag':{
        'firstname':'shreya',
        'lastname':'Bagde',
        'Location':'Nagpur'

    },
     'prajbag':{
        'firstname':'prajakta',
        'lastname':'patil',
        'Location':'Chennai'

    }
}

for data in users:
   print (data,users[data])
print(users['kastubag']["firstname"],users['kastubag']["Location"])   
