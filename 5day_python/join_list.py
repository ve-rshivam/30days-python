# Join the following lists:

# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
compiled_list = front_end + back_end
print(compiled_list)

# 2nd method
front_end.append(back_end)
print(front_end)

# After joining the lists in previous question.
# Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.

full_stack = compiled_list.copy()
print(full_stack)
full_stack.insert(5,'Python')
full_stack.insert(6,'SQL')
print(full_stack)