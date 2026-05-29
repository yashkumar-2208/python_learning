marks = [74,76,83,89,50]
extra_marks = [20,40,60]
print(marks)
marks.extend(extra_marks) #extend = this add two lists in one list.
print(extra_marks)
marks.append(58) #append = adding any number in the end of the list, this causes changing of the original list to modified list.
marks.pop() #pop = it removes the last number.
print(marks)

'''Common Lists Methods.'''
# my_list = [1, 2, 3]
 
# my_list.append(4)   # [1, 2, 3, 4]
# my_list.insert(1, 99)  # [1, 99, 2, 3, 4]
# my_list.remove(2)   # [1, 99, 3, 4]
# my_list.pop()       # Removes last element -> [1, 99, 3]
# my_list.reverse()   # [3, 99, 1]
# my_list.sort()      # [1, 3, 99]