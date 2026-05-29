#Ques_1: Create a text file notes.txt using Python and write "Learning Python is fun!" into it.
f = open("09_File_IO/notes.txt", "w")
content = "Learning Python is fun!"
f.write(content)
f.close()


#Ques_2: Open notes.txt, read its content, and print it to the console.

f = open("09_File_IO/notes.txt", "r")
content = f.read()
print(content)
f.close()


#Ques_3: Write a program that writes three lines of text to a file tasks.txt.

f = open("09_File_IO/tasks.txt", "w")
string = '''Hey my name is: John
My age is: 20
My skills: Python'''
f.write(string)
f.close()


#Ques_4: Open tasks.txt in append mode and add a new line "Task Completed!".

f = open("09_File_IO/tasks.txt", "a")
line = "\nTask Completed! "
f.write(line)
f.close()


