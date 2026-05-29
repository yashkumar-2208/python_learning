# Write a file called John Doe.txt 

f = open("09_File_IO/John Doe.txt", "w")
string = '''
john doe is nice guy'''
f.write(string)

f.close()