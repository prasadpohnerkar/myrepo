str1 = "This is a string."
str2 = 'ApnaCollage'
str3 = """this is a string"""

#find the greatet number among 3 numbers provided

a=int(input("Enter Number 1:"))
b=int(input("Enter Number 2:"))
c=int(input("Enter Number 3:"))

if(a>=b and a>=c):
    print("a is greatest number")
elif(b>=c):
    print("b is greatest number")
else:
    print("c is greatest number")

# WIP to multiple of 7

num = int(input("Enter a number :"))

if((num % 7) == 0):
    print("Num is multiple of 7")
else:
    print("Num is not multiple of 7");

