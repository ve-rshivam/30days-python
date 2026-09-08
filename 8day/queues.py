from collections import deque               # use this to import the special function like deque
queue = deque(['Shivam', 'Kumar', 'Singh'])
queue.append('Delhi')
queue.append('India')
queue.popleft()
queue.popleft()
print(queue)