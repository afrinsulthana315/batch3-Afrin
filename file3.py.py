DAY:3
'''
#eg:3
length=int(input("enter the number:"))
breadth=int(input("enter the number:"))
if length==breadth:
    print("it is a square")
else:
    print("it is not a square")
#eg:4
n=int(input("enter the number:"))
if n%5==0 and n%7==0:
    print("yes")
else:
    print("no")
#EG:5
price=int(input("enter the price:"))
amount=0
if price>=100000:
    discount=price*(6/100)
    value=price-discount
    amount=value*(15/100)
    print(value+amount)
else:
    tax = price*(5/100)
    total = price+tax
    print("the onroad cost of bike is total is:",total)
# if elif else:
#eg :1
a=7
b=6
c=9
if a>b and a>c:
    print("a is greater")
elif b>a and b>c:
     print("b is greater")
elif c>a and c>b:
     print("c is greater")
#eg:2
#A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.    
mark=int(input("enter mark:"))
if mark>=80 and mark<=100:
   print("a")
elif mark>=60 and mark<80:
   print("b")
elif mark>=50 and mark<60:
    print("c")
elif mark>=45 and mark<50:
   print("d")
else:
   print("fail")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
# using short hand if else
* rules
1.)statement inside the if condition have to be present at first
2.)elif cannot be used in short hand if else
3.)always it have to end with else
a=90
b=60
print("A") if a>b else print("B")
#code to check the given char is vowel or consonant
char = input("enter the char:")
if char=="a" or char=="e" or char=="i" or char=="o" or char=="u":
    print("is vowel")
else:
    print("consonant")
# same
char= input("enter the char:")
str1= "aeiouAEIOU"
if char in str1:
    print("vowel")
else:
        print("consonant")
# shorthand if else
char=input("enter the char:")
str1="aeiouAEIOU"
print("vowels") if char in str1 else print("consonent")
# elif ladder using short hand if else
#eg:1
a=8
b=9
c=7
print("a is greater") if a>b and a>c else print("b is greater") if b>a and b>c else print("c is greater")
#looping
#looping can be implemented using
#for loop
#while loop
# FOR LOOP:
# for loop is used for iteration,if we know the number of times the loop have to run
#it is used to iterate the iterables eg(string,list,tuple,etc...)
#SYNTAX FOR LOOP:
# for userdefined_variable in range of (start,end,step): default step value is 1
# statement
#statement
#statement
#EG:1
#to print the value from 1 to 1- using for loop
for i in range(0,10):
    print(i)
    print("hello")
#EG:2
#INCREMENT
for val in range(23,50,1):
    print(val)
#1
for val in range(1,13,2):
    print(val)
#2
for val in range(1,50,3):
    print(val)
#EG:3
#DECREMENT:
for val in range(10,1,-1):
    print(val)
#EG:4
for val in range(1,10+1):
    print(val)
#method:1
for val in range(1,10+1):
    print('7','x',val,'=',val*7)
# method:2
ans="7 x {}={}"
print(ans.format(val,val*7))
#method:3
print(f"7x{val}={val*7}")
#EG:5
#BREAK STATEMENT:
for val in range(1,10):
    if val ==6:
        break
    print(val)
#1
for val in range(1,10):
        print(val)
        if val ==6:
            break
#2
for val in range(1,10):
            if val ==6:
                print(val)
                break
        
#CONTINIOUS:
for val in range(1,10):
         if val ==6:
             continue
             print(val)
#2
for val in range(1,30):
    if val ==6 or val==8 or val ==21:
        continue
    print(val)
#print the even nnumbers between 20 to 40
for val in range(20,40+1,2):
    print(val)
#1
for val in range(20,41):
    if val %2==0:
        print(val)
#while loop:
# while loop is used with number of times the loop have to run
# to iterate the non iterable the elements while loop is ussed
#syntax of while loop
#initialisation
#while condition:
statement
increment or decrement
#EG:1
# to iterate number from 1 to 10
i=0
while i<11:
    print(i)
    i=i+1
    '''
#EG:2
#to decrement using while loop
i=0
while i>0:
 print(i)
i-=1




















    
