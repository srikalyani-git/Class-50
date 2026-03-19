with open("codingal.txt") as file1:
    file1r = file1.read()

with open("file2.txt") as file2:
    file2r = file2.read()

file1r += "\n"
file1r += file2r
print("Meringing two files..")
with open("file3.txt","w") as file3:
    file3.write(file1r)