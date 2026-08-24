# Write a script that prompts the user to enter number of years. 
# Calculate the number of seconds a person can live. Assume a person can live hundred years

year = float(input("Enter number of years you have lived: "))
live = year * 365 * 24 * 60 * 60

print(f"You have lived for {live} seconds.")