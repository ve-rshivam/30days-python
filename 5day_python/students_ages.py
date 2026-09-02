# The following is a list of 10 students ages:
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
# Add the min age and the max age again to the list
# Find the median age (one middle item or two middle items divided by two)
# Find the average age (sum of all items divided by their number )
# Find the range of the ages (max minus min)
# Compare the value of (min - average) and (max - average), use abs() method

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print(max(ages))
print(min(ages))
ages.append(max(ages))
print(ages)
ages.append(min(ages))
print(ages)
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

if len(ages) % 2 == 0:
    median = (ages[5] + ages[6]) / 2
    print(f'Median: {median}')
else:
    median = (ages[5] + 1) / 2
    print(f'Median: {median}')
average = sum(ages) / len(ages)
print(average)
range1 = max(ages) - min(ages)
print(range1)
min_average = min(ages) - average
print(min_average)
max_average = max(ages) - average
print(max_average)