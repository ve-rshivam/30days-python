# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, 
# city and address as keys for the dictionary
student = {}
student['first_name'] = 'Shivam'
student['last_name'] = 'Singh'
student['gender'] = 'male'
student['is_married'] = False
student['skills'] = ['Python']
student['country'] = 'India'
print(student)

# Get the length of the student dictionary
print(len(student))

# Get the value of skills and check the data type, it should be a list
value_skills = student['skills']
print(value_skills)
print(type(value_skills))

# Modify the skills values by adding one or two skills
student['skills'].append('FastAPI')
student['skills'].append('HTML')
print(student)

# Get the dictionary keys as a list
keys = student.keys()
print(keys)

# Get the dictionary values as a list
values = student.values()
print(values)

# Change the dictionary to a list of tuples using items() method
print(student.items())
print(student)

# Delete one of the items in the dictionary
student['first_name'] = 'Shivam'
student['last_name'] = 'Singh'
student['gender'] = 'male'
student['is_married'] = False
student['skills'] = ['Python']
student['country'] = 'India'
del student['is_married']
print(student)

# Delete one of the dictionaries
del student
# print(student)