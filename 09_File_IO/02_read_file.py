#rt = Read file in text mode
#rb = Read file in binary

f = open("09_File_IO/yash.txt", "r")
content = f.read()
print(content)
f.close() 

