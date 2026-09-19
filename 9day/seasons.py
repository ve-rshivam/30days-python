# Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. 
# If the user input is: September, October or November, the season is Autumn. December, January or February, 
# the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer.
month = str(input('Enter a month name: ')).strip().lower()

if month == 'september' or month == 'october' or month == 'november':
    print('This is Autumn.')
elif month == 'december' or month == 'january' or month == 'february':
    print('This is Winter.')
elif month == 'march' or month == 'april' or month == 'may':
    print('This is Spring.')
elif month == 'june' or month == 'july' or month == 'august':
    print('This is summer.')
else:
    print('Invalid month entered.')          