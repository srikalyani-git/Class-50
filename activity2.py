import os
file = open("newfile.txt","x")
file.close()
print("Checking if file exists or not...")
if os.path.exists("newfile.txt"):
    print("File found!!")
    os.remove("newfile.txt")
    print("File removed")
else:
    print("File does not exist")

file = open("newfile.txt","w")
file.write("This is some text")
file.close()
os.rmdir("C:/Users/srika/OneDrive/Desktop/Web_Development/Class 50/fold")