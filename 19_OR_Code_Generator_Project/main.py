#pip install qrcode (a python library)

import qrcode

url = input("Enter the url here: ")
filename = input("Enter the filename you wants to save as:")

if not(filename.endswith(".png")):
    filename = filename + ".png"

img = qrcode.make(url)
img.save(filename)