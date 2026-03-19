with open("codingal.txt", "w") as f:
    f.write("Hi my name is bhavishya")
f.close()

with open("codingal.txt","r") as r:
    file = r.readlines()
    print("Words in this file are")
    for line in file:
        word = line.split()
        print(word)

r.close()
