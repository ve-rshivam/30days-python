person = {
    'first_name': 'Shivam',
    'last_name' : 'Kumar',
    'age' : 19,
    'is_married' : False,
    'country' : 'India',
    'skills' : ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address' : {                                               
        'street' : 'Unknown',                                   
        'city' : 'Delhi',
        'pin_code' : 110001 
    }
}
#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, 
# Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, 
# Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
#  * If the person is married and if he lives in Finland, print the information in the following format:

if 'skills' in person:
    print(person['skills'][(((len(person['skills']))//2))])
else:
    print('not exist')
if 'skills' in person:
    if 'Python' in person['skills']:
        print(person['skills'][4])
else:    
    print('not exist')

if 'skills' in person:
    skills_set = set(person.get('skills', []))       
    if skills_set == {'Javascript', 'React'}:
        print('He is a front end developer.')
    elif {'React', 'Node', 'MongoDB'}.issubset(skills_set):
        print('He is a fullstack developer.')
    elif {'Node', 'Python', 'MongoDB'}.issubset(skills_set):
        print('He is a backend developer.')
    else:
        print('unknown title')

if person.get('is_married') and person.get('country') == 'India':
    print(f'{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.')
else:
    print(f'{person['first_name']} {person['last_name']} lives in {person['country']}. He is Unmarried.')