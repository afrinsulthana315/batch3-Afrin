#day 2:
'''
a,b,c=3,1,5
print(a,b,c)
a,b=c=7,8
print(a)
print(b)
print(c)
a=b, c=4,2
print(a,b,c)
#swapping of variables
a=3
b=15
temp=a
a=b
b=temp
print(a,b)
#eg:2
a=a+b
b=a-b
a=a-b
print(a,b)
#eg:3
a=a*b
b=a/b
a=a/b
print(a,b)
print(int(a),int(b))
#id()--> used to find the memory address of the variable
a=15
print(id(a))
a=52
b=41
print(id(a))
print(id(b))
#keywords
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
print(type(keyword.kwlist))
#literals:
#literal is the constant value assigned to a variable
#a=78#a is a variable
#A=78 #A i s aconstant
#hash()
n1=89+9j
print(hash(n1))
f1=[7,8,9]
print(hash(f1))
a=9
b=9
b=90
print(id(a))
print(id(b))
#Arithmatic operator
a=8
b=7
c=8
print(a-b-c)
print(a+b+c)
n1=eval(input("enter the value:"))
print(type(n1))
a=4
b=8
print(a/b)
print(a%b)
# floor division
a=5836835
b=65854
print(a/b)
print(a//b)
#used for power of a number
print(8*16)
print(2**4)
a=8
a+=2
print(a)
a=30
a-=5
print(a)
#comparision
a=8
b=4
print(a>b)
a=12
b=4
print(a==b)
a=7
b=4
print(a&b)
a=7
print(~a)
#logical
a=6
print(a>3 and a<10)
print(not(a>8 and a<10))
#identify
#is is not
# it is used to compare the memory location that the values stored
a=8
b=8
print(a is b)
print(a==b)
a=[1,2,3]
b=[1,2,3]
print(a is not  b)
#member ship operator
# in,not in
l1=[3,11,15,20]
num=3
print(num in l1)
# conditional statement
# if,elif,else
#eg:1
a=6
if a:
    print("hello")
#eg:2
a=6
if a>3:
    print("yes")
else:
    print("no")
#eg:3
if 7>8:
    print("hello")
    print("no")
#eg:4
a=0
a=None
a=False
a=""
if a:
 print("yes")
else:
 print("no")
# a number is even or odd
n=int(input("enter a number:"))
if n%2==0:
    print(n,"is even")
else:
        print(n,"is odd")
        '''
#name,age,nationality
name=(input("enter a name:"))
age=int(input("enter a age:"))
nationality=input("enter the nation:")
if age>18 and nationality=="indian":
    print("eligible")
else:
    print("not eligible")


































