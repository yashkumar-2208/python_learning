def sum(a,b):
    print("Hey buddy!")
    c = a+b
    global z #modify global z
    z = 5
    return c

z = 3
print(sum(4,8))
print(z)