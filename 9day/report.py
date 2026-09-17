# Write a code which gives grade to students according to theirs scores:
# ```sh
# 90-100, A
# 80-89, B
# 70-79, C
# 60-69, D
# 0-59, F
# ```
 
# name = str(input('Enter your name: '))
marks = int(input('Enter your marks: '))
if marks >= 90:
    print('A')
elif marks >= 80 and marks < 90:
    print('B')   
elif marks >= 70 and marks < 80:    
    print('C')
elif marks >= 60 and marks < 70:
    print('D')    
else:
    print('F')    