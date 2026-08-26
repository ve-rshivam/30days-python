# Declare a variable named company and assign it to an initial value "Coding For All".
# Print the variable company using print().
# Print the length of the company string using len() method and print().
# Change all the characters to uppercase letters using upper() method.
# Change all the characters to lowercase letters using lower() method.
# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
# Cut(slice) out the first word of Coding For All string.
# Check if Coding For All string contains a word Coding using the method index, find or other methods.
# Replace the word coding in the string 'Coding For All' to Python.
# Change "Python for Everyone" to "Python for All" using the replace method or other methods.
# Split the string 'Coding For All' using space as the separator (split()) .

company = 'Coding For All'
print(company)                                  # print company as it is
print(len(company))                             # print the length of charcters present in company including space
print(company.upper())                          # convert all the lowercase to uppercase and then print
print(company.lower())                          # convert all uppercase to lowercase and then print   
print(company.capitalize())                     # convert the first charcter of string in capital letter
print(company.title())                          # convert the firsst letter of every word in to capital letter 
print(company.swapcase())                       # convert all uppercase to lowercase and lowercase to uppercase
print(company[0:6])                             # 0 & 6 index value here 6 is for upto
sub_string = 'Coding'
print(company.index(sub_string))                # if coding is found in word then it print its index number if not found then give error
print(company.find(sub_string))                 # if coding is found in word then it print its index number if not found then print -1
print(company.replace('Coding', 'Python'))      # it will replace 'Coding' to 'Python'
print(company.replace('All', 'Everyone'))       # it will replace 'All' to 'Everyone'
print(company.split())                          # it will split all the word of company into seprate using 'commas'

# What is the character at index 0 in the string Coding For All.
# What is the last index of the string Coding For All.
# What character is at index 10 in "Coding For All" string.
print(company[:1])                              # index value 1 is here for upto
print(company.rfind('l'))                       # it gives the last index value of company i.e. 13
print(repr(company[10]))                        # use for making space visible  by using this we can print the value of index 10