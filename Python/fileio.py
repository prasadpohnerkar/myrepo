import os
f = open("demo.txt","a")
print(f.write("With AI , I will automate the tasks\n"))
#print(f.read())
f.close()

with open("demo.txt","r") as f:
    print(f.read()) 

#os.remove("demo.txt")