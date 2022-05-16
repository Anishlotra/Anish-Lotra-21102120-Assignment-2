#Question 1
a="Python is a case sensitive language"
print("The Length of the Input String is",len(a))
print("Reverse order of the string is-",a[::-1])
print(a[10:-9])
print(a.replace("a case sensitive","object oriented"))
print("Index of 's' is",a.index('a'))
print(a.replace(" ",""))

#Solution 1

#The Length of the Input String is 35
#Reverse order of the string is- egaugnal evitisnes esac a si nohtyP
#a case sensitive
#Python is object oriented language
#Index of 's' is 10
#Pythonisacasesensitivelanguage

#Question 2
b=input("Enter your Name")
c=int(input("Enter your SID"))
d=input("Enter your Department Name")
e=float(input("Enter your CGPA"))
print("Hey,",b,"Here!\nMy SID is",c,"\nI am from",d,"department and my CGPA is",e)

#Solution 2

#Hey, Anish Lotra Here!
#My SID is 21102120 
#I am from Civil Engineering department and my CGPA is 9.0

#Question 3
a=56
b=10
print("a =",a)
print("b =",b)
print("Value of a&b is",a&b)
print("Value of a|b is",a|b)
print("Value of a^B is",a^b)
print("Value of a<<2 is",a<<2)
print("Value of b<<2 is",b<<2)
print("value of a>>2 is",a>>2)
print("Value of b>>4 is",b>>4)

#Solution 3

#a = 56
#b = 10
#Value of a&b is 8
#Value of a|b is 58
#Value of a^B is 50
#Value of a<<2 is 224
#Value of b<<2 is 40
#value of a>>2 is 14
#Value of b>>4 is 0

#Question 4
a=input("Enter the Input")
b=("name" in a)
if b==True:
    print("Yes")
else:
    print("No")

#Solution 4

#1st
#Enter the InputMy name is Anish Lotra
#Yes

#2nd
#Enter the InputMyself Anish Lotra
#No

#Question 5
a = int(input("Enter first length\n"))
b = int(input("Enter second length\n"))
c = int(input("Enter third length\n"))
if a+b<=c or a+c<=b or c+b<=a:
    print("No")
else:
    print("Yes")

#Solution 5

#Enter first length
#20
#Enter second length
#50
#Enter third length
#60
#Yes


#Question 6
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
num=a^b
Count_flipped_bit=0
while(num!=0):
    num=num&(num-1)
    Count_flipped_bit+=1
print("Number of bits needed to be flipped to convert a to b is:",Count_flipped_bit)

#Solution 6

#Enter the number:5
#Enter the number:9
#Number of bits needed to be flipped to convert a to b is: 2


