#DAY:9
#find the uncommon words from 2 strings
'''
s1="hell0 how are you"
s2="hello how is"

s1=s1.split(" ")
s2=s2.split(" ")

for val in s1:
    if val not in s2:
        print(val)
for val in s2:
    if val not in s1:
        print(val)
# 3.)Wrire a code print the 8th fibanochi number
num=8
n1=0
n2=1
for val in range(num):
    ans=n1+n2
    print(ans)
    n1=n2
    n2=ans
    
#method 1
num=8
n1=0
n2=1
for val in range(num):
    ans=n1+n2
    n1=n2
    n2=ans
print(ans)

#constructors
#eg:2
#unparameterised constructor
class profile:
    def __init__(self):
        print("hello world")
obj = profile()
obj.__init__() #<-- if we call the function it will print 2 times
#EG:3
#parameterised constructor
class profile:
    def __init__(self,id,name,age):
        print(id,name,age)
obj = profile(15,"aff",20)

#EG:4
class c1:
    name='sid'
    place='cbe'
    def m1(self):
        print(self.name,self.place)
object =c1()
object.m1()

# method 1:
class c1:
   email = "hsgdhv@1213"
   def m1(self):
    name='sid'
    place='cbe'    
    print(name,place)
    print(self.email)
object =c1()
object.m1()

#
#EG:5
class c1:
    def m1(self):
        name ="sid"
        age=20
        return name,age
    def display(self):
        print(self.m1())
object = c1()
object.display()

#
EG:6
class class1:
 
def __init__(self):
       self.name = 'sid'
       self.email = 'sid@gmail.com'
        #return name,email #-->cannot use return with constructor
       
def display(self): 
        print(self.name, self.email)
c1=class1()
c1.display()

#INHERITANCE:
#THE PROCESS OF UTILISING THE METHODS AND ATTRIBUTES OF PARENT CLASS 
#THROUGHT THE OBJECT OF CHILD CLASS IT IS CALLED AS INHERITANCE
#5 TYPES OF INHERITANCE
#single INHERITANCE
#multilevel INHERITANCE
#multiple INHERITANCE
#hybrid INHERITANCE
#herarchical INHERITANCE

#1.single INHERITANCE:
# it has only one parent class and only one child class
#EG:1
class parent:
   def m1(self):
      print("i am parent class")
                                                   
class child(parent):
   def m2(self):
      print("i am child class")
      
obj = child()
obj.m1()

#eg:2  
class c1:
   def __init__(self):
      print("i am constructor from parent class")
class child1(c1):
   pass
obj = child1()

#eg:3
class parent:
   name = "afrin"
class child(parent):
   name ='name1'
   defdisplay(self):
      print(self.name)
d =child()
d.display()

#multilevel inheritance
# ? Eg:1
class voice:
    def sound(self):
        print("All the animals have their own voices")

class dog(voice):
    def dog_voice(self):
        print("bark")
        
class cat(dog):
    def cat_voice(self):
        print("Meow")
        
class parrot(cat):
    def dog_voice(self):
        print("speak")

all = parrot()
all.dog_voice()
all.cat_voice()
all.sound()
all.parrot_voice()

#multiple inheritance
# it ha smultiple parent and one child
class while_pertol:
    def function_w(self):
        print("used to Airplans")

class Organic_petrol:
    def function_o(self):
        print("used for Bike, cars")
class premium_petrol:
    def function_p(self):
        print("spots cars, bikes")
class petrol(while_pertol, Organic_petrol, premium_petrol):
    def defanition(self):
        print("Petrols types")
p=petrol()
p.defanition()
p.function_o()

#
# Eg:2
# MRO---> Method resolution Order
class addition:
    def add(self, a, b):
        print(a+b)
    def mul(self,a,b):
        print(a%b)
class subract:
    def sub(self, a, b):
        print(a-b)
class multiply:
    def mul(self, a, b):
        print(a*b)
class division(addition, subract, multiply):
    def div(self, a, b):
        print(a/b)
calc=division()
calc.add(3,4)
calc.mul(5,2)

# herarchical inheritance
#? The one parent classe will asct as parent for all the child classes
class catagory:
   def weight(self, weight):
     print(weight)
def display(self, color, taste):
   print(color, taste)
class Tomato(catagory):
 def tomato_specs (self):
  color="black" 
taste = "neutral taste"
self.display(color, taste)
class carrot (catagory):
 def carrot_specs (self):
  color="green"
c=carrot()
c.carrot_specs()
c.weight("30gms")

# hybrid Inheritance
 # The combination of above 4 inheritance is called Hybrid inheritance
class c1:
    def m1(self):
        print("Class 1")

class c2(c1):
    def m2(self):
        print("Class 2")

class c3(c2):
    def m3(self):
        print("Class 3")

class c4(c2):
    def m4(self):
        print("Class 4")
        
    def m3(self):
        print("i am m3 from c4")

class c5(c3):
    def m5(self):
        print("Class 4")  

class c6(c5, c4, c2, c1):
    def m6(self):
        print("Class 6")
obj = c6()
obj.m3()
#polymorphism:
#poly--many,morph-->form
# a function which has the ability to perform more than 1 function
#polymorphism in operators
#+
print(8+8)
print('k'+'1')
print([1,2,3]+[5,6])
'''
#*
print(6*7)
l1 = {1,2,3,4,5,6}
print(*l1)
def f1(*args)
l1 = [1,2,3,4]
print(l1*10)



























    
