file = open("file2.txt","w")
file1 = open("codingal.txt","r")
data = file1.readlines()
name = set()
for x in data:
    if x not in name:
        file.write(x)
        name.add(x)

file.close()
file1.close()