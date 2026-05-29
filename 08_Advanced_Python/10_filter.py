def is_greater_than_9(x):

    if x>9:
        return True
    else:
        return False
    
a = [1,3,45,75,657,675,987,342,97,4]

new = list(filter(is_greater_than_9, a))
print(new)


print('------')

b = [27,356,46,43,6,8,23,87]
news = list(filter(lambda x: x>9, a))
print(news)

















