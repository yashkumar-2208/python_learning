#Ques_1: Create a string variable name with your full name. Print:
# The first character
# The last character
# The length of the string

name = "Yash Kumar"
print(name[0:4])
print(name[5:10])
a = len(name)
print(f"{a} is the length of {name}")

#Ques_2: Concatenate two strings: "Hello" and "World" with a space in between.
text = "Hello", "World"
a = " ".join(text)
print(a)

 #Ques_3: Given text = "Python Programming", do the following:
# Print the first 6 characters
# Print the last 6 characters
# Print every second character from the string
#Reverse the string text using slicing.
text = "Python Programming"
print(text[:6])
print(text[13:18])
print(text[1])
print(text[8])
print(text[::-11])


# Ques_4: Take the string "  i love python programming  " and:

# Remove extra spaces from both ends
# Convert it to title case
# Count how many times "o" appears

text = "  i love python programming  "
print(text.strip())
print(text.title())
print(text.count("o"))

# Ques_5: Check if the string "123abc" is alphanumeric.

text = "123abc"
print(text.isalpha())


#Ques_5:  using f-strings.create a sentence:
# "My name is John and I am 25 years old."
# by passing "John" and 25 as variables.

name = "John"
age = 25
print(f"My name is {name} and I am {age} years old.")



# Ques_6: Given sentence = "Coding in Python is fun", replace "fun" with "awesome" and print it.
# Find the index of the word "Python" in sentence.
# Convert the entire sentence to uppercase and print it.

sentence = "Coding in Python is fun"
print(sentence.replace("fun", "awesome"))
print(sentence.index("Python"))
print(sentence.upper())


#Ques_7: Write a program that counts how many vowels are in a given string.

sentence = "My name is Yash"
sum  = 0
vowels = ['a','e','i','o','u']
for char in sentence.lower():
    if (char in vowels):
        sum += 1
print(f"There are {sum} vowels in this sentence")

#Ques_8: Take a user input string and check if it is a palindrome (same forwards and backwards).
while True: 
    string1 = input("Enter any word to check if it is palindrome or not: ")
    if (string1 == string1 [::-1]):
        print("The string is palindrome")
    else:
        print("No it is not a palindrome")






























