#Create a list containg the table of 5
'''Common Method: '''
a = 5
for i in range(1,11):
    print(f"5 X {i}",5*(i))


'''Different method:'''
b = 6
table = []
for i in range(1,11):
    table.append(5*i)
print(table)


'''Short method: List comprehensions.'''
table = [5*i for i in range(1,11)]
print(table)
