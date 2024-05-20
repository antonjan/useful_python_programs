names = ['reza', 'zahra', 'sara', 'ali']
i = [4, 2, 5, 1]
sortedList =  [val for (_, val) in sorted(zip(i, names), key=lambda x:x[0])]
print(sortedList)
