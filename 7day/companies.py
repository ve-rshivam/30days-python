it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# Find the length of the set it_companies
print(len(it_companies))
# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)
# Insert multiple IT companies at once to the set it_companies
it_companies.update(['Accenture', 'Capgemini'])              # while using update make sure we write items in square brackets
print(it_companies)            
# Remove one of the companies from the set it_companies
it_companies.pop()
print(it_companies)
# What is the difference between remove and discard
it_companies.remove('IBM')
print(it_companies)
it_companies.discard('Google')
print(it_companies)         # in remove when the item is not find in set then it give a error but while using discard it does not give any error in this case