# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python
variable1 = '30DaysOfPython'
variable2 = 'thirty_days_of_python'

print(variable1.isidentifier())             # it check string name is valid it is False because it start number
print(variable2.isidentifier())             # it gives True because it starts with charcter