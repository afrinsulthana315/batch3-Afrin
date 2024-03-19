#DAY:8
#3
'''
def profile(name,age,place):
   txt="my name is {}. i am {} years old. i am from {}."
   print(txt.format(name,age,place))
profile("tif",29,"kdp")
#4
#function with return statement
#return
#1. a variable declare inside the function can b acccessed outside the function using return
#2.return does not print anything
# 3. we cannot write any code below return statement

def f1(a,b):
    c = a*b
    return c
print(f1(6,8))
obj  = f1(6,8)
obj1 = f1(4,6)

def gracemark(object):
    print(object+4)
gracemark(obj)
gracemark(obj1)

#123
def palindrome(n):
    string =str(n)
    rev= str(n)[::-1]
    if string==rev:
        print(n,'palindrome')
    else:
        print('not palindrome')
a=int(input("enter the value:"))
palindrome(a)

#based on the declaration of parameter and args
# functions are divided into 5 categories
#positional args
#keyword args
#default args
#variable length args
#keyword variable length args

#positional args
# the position of parameters have to be same as position of argument
#EG:1
#unexpected output
def profile(name, phone,mark):
    txt='my name is {}.my phone number is {}.i got {} marks.'
    print(txt.format(name, phone,mark))
profile(365865464,'siddu',97)
#keyword args
#eg:1
#to overcome the disadvantage of position args,we use keyword arg
#it is the process of instalising the parameter eith the args while calling the function
#def profile(name,phone,mark):
 #    txt='my name is {}.my phone number is {}.i got {} marks.'
  #  print(txt.format(name, phone,mark))
#profile(name="anda",mark=100,phone=0123456)
# exception of keyword args function

def profile(name,phone,mark):
    txt='my name is {}.my phone number is {}.i got {} marks.'
    print(txt.format(name, phone,mark))
#profile(name='anda',5242547,marks=69)# error-->positional args follow keyword
#profile(5465468754,name='anda',mark=85)#error-->name has multiple values
profile('anda',mark=97,phone=545747)

#DEFAULT ARGS
#the method of assigning the argument to the parameter while dclaring the function
#EG:1
def profile(name,phone,place='kadapa'):
    txt='my name is {}.my phone number is {}.i am from  {}.'
    print(txt.format(name, phone,place))
    
profile('anda',2689898)

#eg:2
def profile(name,phone,place='kadapa'):
    if place == "kadapa" or place=="KADAPA" or place=="kadapa":
         txt='my name is {}.my phone number is {}.i am from  {}.'
         print(txt.format(name, phone,place))
    else:
        print("you are not eligible to signup")
profile('anda',2689898,)

# variable length params
#eg:1
name="sid",'name2','name3'
def profile(*name):
    for val in name:
        print("my name is",name)
profile("sid",'name2','name3')

#EG:2
def profile(age, *name):
    for val in name:
        print("my name is",val,"my age is",age)
profile(28,"sonu",'name3','name3')

#keyword variable length args
#kwargs-->which is used to provide the args in the form of key value pair
#eg:1
def price(**price_list):
    print(price_list)
price(shirt=1000,iphone=80000)
d1={"a":100,"b":200,"c":300}
d1=dict(a=100,b=200,c=300)
print(d1)

#eg:2
#n=5
#d1={1:1,2:4,3:9,4:16,5:25}
n=int(input("enter the number:"))
d1={}
for val in range(1, n +1):
    d1[val]=val**2
print(d1)
# function method
def dict(n):
    d1={}
    for val in range(1, n +1):
        d1[val]=val**2
    print(d1)
dict(6)

#object oriented programming:
#the paradigms of objects oriented programming language are
#class
#objects
#inheritance
#polymorphism
#abstraction
#encapsulation

# class is a BLUE PRINT OF AN OBJECT
#eg:1
l1=[1,2,3,4,5,6]
class c1:
    name1 = "sidhu"
    print(name1)
#eg:2
class person:
    name = "sidhu"
c = person()
print(c.name)

#eg:3
#create of a method
# when the function is created with a class is called as method
class person:
    def display(person):
        print("hello welcome to classes")
p=person()
p.display()

#4
#method with parameter:
class person:
    def display(person,name,age):
        print(name,age)
p=person()
p.display("bablu",20)
'''

#eg:5
class person1:
    fname="bablu"
    lname="s"
    def first_name(self):
        print(self.fname)
    def full_name(self):
        print(self.fname+" "+self.lname)
p=person1()
p.first_name()
p.full_name()

#eg:6
# constructors  -->__init__()
# This is a special method which has the ability to execute to itself without
# calling it manullay through the process of instantiation
class profile:
    def _init_(self):
        print("hey")
p = profile()
p._init_()





























