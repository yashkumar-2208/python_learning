with open("09_File_IO/yash.txt") as f:
    content = f.read()
    print(content)

#no need to write f.close(), (because file is already closed by default)