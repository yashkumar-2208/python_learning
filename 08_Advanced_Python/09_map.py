numbers = [1,2,3,4,5,6,7,8]

def square(x):
    return x*x

new = list(map(square, numbers))
print(new)

print("-------")

number = [45,675,9768,21]
news = list(map(lambda x: x*x, number))
print(news)