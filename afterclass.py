import os
with open("Sample_File.txt","w") as file1:
    file1.write("Hi, My name is Bhavishya and I'm 14 years old")

with open("Sample_File.txt","r") as file1:
    data = file1.readlines()
    print("Words in this file are:")
    for line in data:
        word = line.split()
        print(word)

if os.path.exists("My_File.txt"):
    print("File exists....")
    

else:
    file2 = open("My_File.txt","w")
    file2.write("Hi, My name is Bhavishya and I'm 14 years old")

os.remove("sample_doc.txt")