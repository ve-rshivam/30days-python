# # Declare a list variable named it_companies and assign initial values 
# # Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

it_companies  = ['Facebook','Microsoft','Apple','IBM','Oracle','Amazon']
print(it_companies)

# Print the number of companies in the list
print(len(it_companies))

# Print the first, middle and last company
print(it_companies[0])
print(it_companies[((len(it_companies))//2)-1])
print(it_companies[len(it_companies)-1])

# Print the list after modifying one of the companies
it_companies[2] = 'Accenture'
print(it_companies)
it_companies  = ['Facebook','Microsoft','Accenture','IBM','Oracle','Amazon']

# Add an IT company to it_companies
it_companies.append('Capgemini')            # it will add item in the last index number
print(it_companies)
# Insert an IT company in the middle of the companies list
it_companies = ['Facebook', 'Microsoft', 'Accenture', 'IBM', 'Oracle', 'Amazon', 'Capgemini']

it_companies.insert((len(it_companies) // 2), 'TCS')                # it will add item in the index value which was assigned
print(it_companies)
it_companies  = ['Facebook','Microsoft','Accenture','IBM','TCS','Oracle','Amazon']

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies = ['Facebook', 'Microsoft', 'Accenture', 'TCS', 'IBM', 'Oracle', 'Amazon', 'Capgemini']
for i in range(len(it_companies)):
    if it_companies[i] != 'IBM':
        it_companies[i] = it_companies[i].upper()               # this will only convert 'Facebook' in uppercase
        break                                                   # if we remove break then it convert all of them into uppercase except 'IBM'
print(it_companies)
# Join the it_companies with a string '#;  '
it_companies = ['Facebook', 'Microsoft', 'Accenture', 'TCS', 'IBM', 'Oracle', 'Amazon', 'Capgemini']

it_companies1 = '#'.join(it_companies)
print(it_companies1)
# Check if a certain company exists in the it_companies list.
it_companies = ['Facebook', 'Microsoft', 'Accenture', 'TCS', 'IBM', 'Oracle', 'Amazon', 'Capgemini']
print('Facebook' in it_companies)
print('Oracle' in it_companies)
# Sort the list using sort() method
it_companies.sort()                 # it will print alphabetically ascending order
print(it_companies)
it_companies.sort(reverse=True)     # it will print alphabetically descending order
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies = ['Facebook', 'Microsoft', 'Accenture', 'TCS', 'IBM', 'Oracle', 'Amazon', 'Capgemini']
it_companies.sort(reverse=True)     # it will print alphabetically descending order
print(it_companies)

# Slice out the first 3 companies from the list
it_companies = ['Facebook', 'Microsoft', 'Accenture', 'TCS', 'IBM', 'Oracle', 'Amazon', 'Capgemini']
it_companies1 = it_companies[3:]
print(it_companies1)
# Slice out the last 3 companies from the list
it_companies = ['Facebook', 'Microsoft', 'Accenture', 'TCS', 'IBM', 'Oracle', 'Amazon', 'Capgemini']
it_companies1 = it_companies[:5]
print(it_companies1)
# Slice out the middle IT company or companies from the list
it_companies = ['Facebook', 'Microsoft', 'Accenture', 'TCS', 'IBM', 'Oracle', 'Amazon', 'Capgemini']

print(it_companies[(len(it_companies) // 2) - 1])

# Remove the first IT company from the list
it_companies = ['Facebook', 'Microsoft', 'Accenture', 'TCS', 'IBM', 'Oracle', 'Amazon', 'Capgemini']
del it_companies[0]
print(it_companies)

# Remove the middle IT company or companies from the list
it_companies = ['Facebook', 'Microsoft', 'Accenture', 'TCS', 'IBM', 'Oracle', 'Amazon', 'Capgemini']
del it_companies[(len(it_companies) // 2) - 1]
print(it_companies)
# Remove the last IT company from the list
it_companies = ['Facebook', 'Microsoft', 'Accenture', 'TCS', 'IBM', 'Oracle', 'Amazon', 'Capgemini']
del it_companies[len(it_companies) - 1]
print(it_companies)
# Remove all IT companies from the list
it_companies = ['Facebook', 'Microsoft', 'Accenture', 'TCS', 'IBM', 'Oracle', 'Amazon', 'Capgemini']
it_companies.clear()
print(it_companies)
# Destroy the IT companies list
it_companies = ['Facebook', 'Microsoft', 'Accenture', 'TCS', 'IBM', 'Oracle', 'Amazon', 'Capgemini']
del it_companies
# print(it_companies)               # now it will give a