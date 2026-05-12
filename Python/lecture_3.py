marks = [95.4,86.5,75.5,98.6,99.5]
print(marks)
print(type(marks))
print(len(marks))

tup=(2,3,1,4,1,5,3,2,1)
print(tup)
print(type(tup))

#WAP to check if list contains Palindrom

pal = [1,2,3,2,1]
pal1 = pal.copy()
pal1.reverse()

if(pal == pal1):
    print("pal is a Palindrom list")
else:
    print("pal is not a Palidrom list")

def CalSum(a,b):
    return a+b
    
print(f"Sum of two numbers is",CalSum(3,5))

#WAF to print the lenght of the list

lst = [1,2,3,4,5]
def ListLen(lst):
    return len(lst)

print("Length of the list is ",ListLen(lst))

#WAF to print the elements of a list in single line
lst = [1,2,3,4,5]
def PrintList(lst):
    for i in lst:
        print(i,end=" ")

print("Elements of the list are : ",end="")
PrintList(lst)

#WAF to print n factorial of a number
def Factorial(n):
    if n == 0:
        return 1
    else:
        return n * Factorial(n-1)

print("\nFactorial of 5 is ",Factorial(5))

#WAF to convert USD to INR
def USDToINR(usd):
    inr = usd * 95
    return inr

print("1200 USD is equal to ",USDToINR(1200)," INR")

#WAF to show a number using recursion
def ShowNum(n):
    if n > 0:
        print(n,end=" ")
        ShowNum(n-1)

print("Numbers from 10 to 1 are : ",end="")
ShowNum(10)  

#WAF to find the greatest number among 3 numbers using function
def Greatest(a,b,c):    
    if(a>=b and a>=c):
        return a
    elif(b>=c):
        return b
    else:
        return c

print("Greatest number among 10, 20, and 30 is : ",Greatest(10,20,30))

#WAF to find factorial of a number using recursion
def Factorial(n):
    if n == 0:
        return 1
    else:
        return n * Factorial(n-1)   
print("Factorial of 5 using recursion is ",Factorial(5))  

#Write a recursive function to find the sum of first n natural numbers
def SumOfNaturalNumbers(n): 
    if n == 0: 
        return 0
    else: 
        return n + SumOfNaturalNumbers(n-1)     
print("Sum of first 5 natural numbers is ",SumOfNaturalNumbers(5))

#Write a recursive function to print all elements of a list
def PrintList(lst, index=0):    
    if index < len(lst):
        print(lst[index], end=" ")
        PrintList(lst, index + 1)   
lst = [1, 2, 3, 4, 5]
print("Elements of the list are : ", end="")
PrintList(lst)  

#Write a recursive function to find the greatest number in a list
def GreatestInList(lst, index=0):    
    if index == len(lst) - 1:
        return lst[index]
    else:
        max_in_rest = GreatestInList(lst, index + 1)
        return max(lst[index], max_in_rest) 
lst = [3, 1, 4, 1, 5, 9]
print("\nGreatest number in the list is : ", GreatestInList(lst))

