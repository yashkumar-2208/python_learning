# Ques_1: Create a list fruits = ["apple", "banana", "cherry"].
# Print the first fruit.
# Replace "banana" with "orange".
# Print the length of the list.

fruits = ["apple", "banana", "cherry"]
print(fruits[ 0])

fruits[1] = "orange"
print(fruits)

a = len(fruits)
print(a)


# Ques_2: Create a list of numbers from 1 to 10.
# Print the first three numbers using slicing.
# Print the last three numbers using slicing.

list = [1,2,3,4,5,6,7,8,9,10]
print(list[:3])
print(list[7:11])

# Ques_3: Start with numbers = [5, 2, 9, 1, 7] and do the following:

# Sort the list in ascending order.
# Append the number 10 to the list.
# Remove the number 2 from the list.

numbers = [5,2,9,1,7]
numbers.sort()
print(numbers)

numbers.append(10)
print(numbers)

numbers.remove(2)
print(numbers)


#Ques_4: Create a list names =s ["Alice", "Bob", "Charlie"] and use the insert() method to add "David" at index 1.
names = ["Alice", "Bob", "Charlie"]
names.insert(1,"David")
print(names)


#Ques_5: Create a tuple coordinates = (10, 20) and print both elements.
#Try to modify the tuple by setting coordinates[0] = 50 — note what happens.
#Convert the tuple to a list, change its first element to 50, and convert it back to a tuple.

coordinates = (10, 20) 
print(coordinates[0])
print(coordinates[1])

#coordinates[0] = 50 #cannot change 
corlist = list(coordinates)
corlist[0] = 50
coordinates = tuple(corlist)
print(coordinates)


#Ques_6: Create a set my_set = {1, 2, 3, 3, 4} and print it. (What happens to duplicate 3?)
#Add 5 to the set, remove 2, and check if 4 is in the set.

my_set = {1, 2, 3, 3, 4}
print(my_set)
my_set.add(5)
print(my_set)
my_set.remove(2)
print(my_set)


#Ques_7: Create two sets:
#a = {1, 2, 3}
#b = {3, 4, 5}
#Find their:
#Union
#Intersection
#Difference (a - b)
'''Ques_7: '''

a = {1,2,3}
b = {3,4,5}
c = a.union()
print(c)

d = a.intersection()
print(d)

e = (a-b)
print(e)


#Ques_8: Create a dictionary student = {"name": "John", "age": 20, "grade": "A"} and:
#Print the value of "name".
#Change "grade" to "A+".
#Add a new key "city" with value "Delhi".

student = {"name": "Jonh", "age": 20, "grade":"A"}
print(student['name'])
student['grade'] = "A+"
print(student)
student['city'] = "Delhi"
print(student)


#Ques_9: Create a dictionary of three friends and their phone numbers. Use:
#keys() to get all names
#values() to get all numbers
#items() to loop over key-value pairs and print them

friends_list = {
    "Yash": 70780000,
    "Himanshu": 910500000,
    "Shubham": 70000000
}

print(friends_list.keys())
print(friends_list.values())
print(friends_list.items())