mixed_type={'Shubham',25,124,True}
more_add={'Rahul',24}
#Add() method==> add element to the set.

mixed_type.add('Trainer')
print('Add method :',mixed_type)
#Add method : {'Shubham', 'Trainer', True, 25, 124}

#Update() method

mixed_type.update(more_add)
print('Update method :',mixed_type)

# Add method : {True, 'Trainer', 'Shubham', 25, 124}
# Update method : {True, 'Trainer', 'Rahul', 'Shubham', 24, 25, 124}

#Discrad() method -> remove specified element

mixed_type.discard('Trainer')
print('Discard_method :',mixed_type)
#Discard_method : {True, 'Shubham', 'Rahul', 24, 25, 124}

#Remove() method

mixed_type.remove('Rahul')
print('Remove Method :',mixed_type)

# #Remove Method : {True, 24, 25, 'Shubham', 124}

#Difference Between Remove and discard

REMOVE==> It will Throw error when there is no data what you want to remove.
         (if there is no 'trainer' data but you did  remove('TRainer' ),it will trow error)

Discard==>It will not Throw error when there is no data what you want to remove.
         (if there is no 'trainer' data but you did  remove('TRainer' ),it will not trow error)
















