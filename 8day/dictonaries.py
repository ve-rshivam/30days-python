# A dictonaries is a collection of unordered, modifiable(mutable) paired(key:value) data type.
# we use curly brackets {} to create a dictonaries or dict() in built function
# Creating a empty dictonaries
empty_dict = {}
print(empty_dict)
person = {
    'first_name': 'Shivam',
    'last_name' : 'Kumar',
    'age' : 19,
    'is_married' : False,
    'country' : 'India',
    'skills' : ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address' : {                                               # in this dictonaries we had created a another dictonaries in it that means that
        'street' : 'Unknown',                                   # in under dictonaries we can create any type of data types like dict, tuple,and any one 
        'city' : 'Delhi',
        'pin_code' : 110001 
    }
}
print(person)               # it will print all the keys and values 
print(len(person))          # it will print the length of keys in a dictonaries
# Accessing the values using directly keys
print(person['country'])
print(person['first_name'])
print(person['address'])
print(['skills'])
print(person['address']['street'])              # this is used to access another dictonaries value using their keys 
# print(person['city'])                           # this will give a error beacuse there is no any one key is defined as city 
# for removing we can use .get() method to removing this Error
print(person.get('city'))                       # now it will give a None value at the place of Error

# Adding a values to the dictonaries
# we can add new values to the dictonaries by first assigning them first keys and them values

person = {
    'first_name': 'Shivam',
    'last_name' : 'Kumar',
    'age' : 19,
    'is_married' : False,
    'country' : 'India',
    'skills' : ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address' : {                                              
        'street' : 'Unknown',                                  
        'pin_code' : 110001 
    }
}
person['job_title'] = 'Student'                 # keys and the values assign to the last index number
person['skills'].append('HTML')                 # .append update the present value by using their keys 
print(person)

# Modify item in dictonaries
person = {
    'first_name': 'Shivam',
    'last_name' : 'Kumar',
    'age' : 19,
    'is_married' : False,
    'country' : 'India',
    'skills' : ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address' : {                                              
        'street' : 'Unknown',                                  
        'pin_code' : 110001 
    }
}
person['last_name'] = 'Singh'
person['age'] = 20
print('Modified data')
print(person)

# Checking keys in dictonaries 
# we use in operator to check if any keys exist in dictonaries
person = {
    'first_name': 'Shivam',
    'last_name' : 'Kumar',
    'age' : 19,
    'is_married' : False,
    'country' : 'India',
    'skills' : ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address' : {                                              
        'street' : 'Unknown',                                  
        'pin_code' : 110001 
    }
}
print('last_name' in person)
print('city' in person)

# Removing key and value pairs from dictonaries
person = {
    'first_name': 'Shivam',
    'last_name' : 'Kumar',
    'age' : 19,
    'is_married' : False,
    'country' : 'India',
    'skills' : ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address' : {                                              
        'street' : 'Unknown',                                  
        'pin_code' : 110001 
    }
}
person.pop('last_name')                 # remove the specific item 
print(person)
person.popitem()                        # remove the last index item 
print(person)
del person['is_married']                # remove the specific item
print(person)

# Changing Dictionary to a list of items
# the items () method change dictonary to a list of tuples

person = {
    'first_name': 'Shivam',
    'last_name' : 'Kumar',
    'age' : 19,
    'is_married' : False,
    'country' : 'India',
    'skills' : ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address' : {                                              
        'street' : 'Unknown',                                  
        'pin_code' : 110001 
    }
}
print(person.items())
# Clearing a dictonary
# if we don't want a item in dictonary we can clear them using clear() method.
person = {
    'first_name': 'Shivam',
    'last_name' : 'Kumar',
    'age' : 19,
    'is_married' : False,
    'country' : 'India',
    'skills' : ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address' : {                                              
        'street' : 'Unknown',                                  
        'pin_code' : 110001 
    }
}
print(person.clear())
# Deleting 
person = {
    'first_name': 'Shivam',
    'last_name' : 'Kumar',
    'age' : 19,
    'is_married' : False,
    'country' : 'India',
    'skills' : ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address' : {                                              
        'street' : 'Unknown',                                  
        'pin_code' : 110001 
    }
}
del person
# print(person)                 # now this will give a error

# Getting dictonary keys as a list
# the keys() method gives all the keys of a dictonary as a list 
person = {
    'first_name': 'Shivam',
    'last_name' : 'Kumar',
    'age' : 19,
    'is_married' : False,
    'country' : 'India',
    'skills' : ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address' : {                                              
        'street' : 'Unknown',                                  
        'pin_code' : 110001 
    }
}
keys = person.keys()
print(keys)

# Getting dictonaries values as a list
# the value() method gives all the value of a dictonaries as a list
person = {
    'first_name': 'Shivam',
    'last_name' : 'Kumar',
    'age' : 19,
    'is_married' : False,
    'country' : 'India',
    'skills' : ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address' : {                                              
        'street' : 'Unknown',                                  
        'pin_code' : 110001 
    }
}
values = person.values()
print(values)