#DAY:5
'''
#COMMON FUNCTIONS FOR LIST:
l1=[6,7,8,9]
print(len(l1))
print(max(l1))
print(min(l1))
#l1=[2,4,8,"p","u"]
#print(max(l1))--->error coz its acombination of int and string
#print(min(l1))--->error coz its acombination of int and string
l1=[6,7,8,9,0,3.5,8.89,-5]
# index-->to get the index value of specific element
print(l1.index(9))
l1=[6,7,8,9,0,3.5,8.89,-5]
#count()---> how many num of times an element is repeated
print(l1.count(6))
#some functions which is specificially used for list
#to add element inside the list
#insert()-->to add element at specific index portion
l1=[6,7,8,9,0,3.5,8.89,-5]
l1.insert(2,"cars")
print(l1)
# to delet element from list
l1=[6,7,8,9,0,3.5,8.89,-5]
l1.pop()
print(l1)
#pop(index value)-->used to delete element at specific index
l1=[6,7,8,9,0,3.5,8.89,-5]
l1.pop(4)
print(l1)
#remove(element)-->used to delete element directly
l1=[6,7,8,9,0,3.5,8.89,-5]
l1.remove(7)
print(l1)
#clear()-->to complete delete all element in list
l1=[6,7,8,9,0,3.5,8.89,-5]
l1.clear()
print(l1)
#del-->to delete the list
l1=[6,7,8,9,0,3.5,8.89,-5]
del l1
print(l1)
l1=[4,5,6,]
l2=[7,8,9]
print(l1+l2)
#or
#extend()---> to combine 2 lists
l1.extend(l2)
print(l1)
l1=[6,7,8,9,0,3.5,8.89,-5]
l2=l1.copy()
print(l2)
print(l1)
print(id(l1))
print(id(l2))
#diff between shallow copy and deep copy
#shalow copy
import copy
l1=[6,7,8,[9,0],[4,89]]
l2=copy.copy(l1)
l1.append(315)
print(l1)
print(l2)
# deep copy-->used to cpoy the list with nested list
#import copy
l1=[6,7,8,[9,0],[4,89]]
print(l1[-1][1]) 
l2= Copy.deepcpoy(l1)
l1[-1].append('cars')
print(l1)
print(l2)
#sort--->ARRANGE ELEMENTS IN LIST IN ASCENDING ORDER OR DESENDING
l1=[9,7,45,315]
l1.sort()#to arrange in ascending order
print(l1)
l1.sort(reverse=True)# to arrange in descending order
print(l1)
# LIST CONSTRUCTOR
l3=((8,9,0))
print(list(l3))
l4=(8,9)
print(list(l4))
# nested list
l1=[8,9,[0,8,7],["p","o",'y'],[8,'t']]
print(l1[-2][1])
print(l1[1:3])
print(l1[1:-1])
# to delete "t" from l1
l1=[8,9,[0,8,7],["p","o",'y'],[8,'t']]
l1[-1].remove('t')
print(l1)
# combine these 2 list in
l1=[8,9,[0,8,7],["p","o",'y'],[8,'t']]
l1[-2].extend(l1[-1])
l1.pop(-1)
print(l1)
#----> tuple:
#1.tuple have to be surrounded by()
#2.the elements inside tuple are not changable
#3.the elements inside tuple are indexed
#4.the elements execute in order
#5.it is heterogeneous
#6.it allow duplicate elements
#EG:1
t1=(8,8,9,6,5.78,[9,0],(6,8),"hey",9+6j)
print(t1)
print(type(t1))
#indexing,slicing are all same as list
l1=(5)
print(type(l1)
#2.
l1=[4]
print(type(l1))
#3.
t1=3,15
print(type(t1))
#len(),min(),max(),index(),count()--> all same as list
# to add element inside tuple-->cnnot add
#cannot delete any element from tuple
#join 2 tuple
t1=(1,2,3)
t2=(4,5,6)
print(t1+t2)
sum()
l1=(8,9,7,6)
print(sum(l1))
#SORT TUPLE
t1 = (8,6,9,0,89)
print(tuple(sorted(t1)))
print(tuple(sorted(t1,reverse=True)))
# iterate list and tuples
#iterate based on elements
l1=[9,8,0,6,5]
for i in l1:
    print(i)
#iterate based on index value
l1=[9,8,0,6,5]
for i in range(0,len(l1)):
    print(l1[i])
# SRTING:
s1='O'
print(type(s1))
#2.
s1="hello world"
print(type(s1))
#indexing and slicing-->same as tuple and list
s1="hello world"
print(s1[0:5])
#common functions
s1="hello world"
print(len(s1))
print(max(s1))
print(min(s1))
#ord()--->used to find the ASCII value of character
s1="u"
print(ord(s1)
# functions of string
s1="hello world"
#to convert all characters to uppercase
print(s1.upper())
#to convert lowercase
s1='KTHKDRHG'
print(s1.lower())
#strip
#left
s1="  moti dom dom"
print(s1.lstrip())
# right
print(s1.rstrip())
print(s1.strip())
#split()-->to split the words in string based on character
s1="  moti dom dom"
print(s1.split("r"))
#
s1="  moti dom dom"
print(s1.count('o'))
print(s1.replace('d','&&'))
#capital=small
s1="HEY there"
print(s1.swapcase())
#title()-->to write the string in form of title
s1='never giveup'
print(s1.title())
#capitalize()
s1='never give up'
print(s1.capitalize())
#join the string
s1="Afrin"
s2="SULTHANA"
print(s1+s2)
'''
#
s1='''how are you
i am fine
hey there
#splitlines()-->used to split the string based on lines
print(s1.splitlines())
#find()
s1="hello world"
print(s1.find('h'))
print(s1.index('w'))
# join()-->
l1=["hey","there"]
print("".join(l1))
print("$".join(l1))
#
s1="welcome to all"
print(s1.endswith('l'))
print(s1.endswith('d'))
#
s1="67"
print(type(s1))
print(s1.isdigit())
# string is reverse manner
s1="welocome to all"
print(s1[::-1])
#EG:1
# to find the number of lower case letters
s1="HEY there you aRE"
count = 0
for i in s1:
    if i. islower():
        count+=1
print("the total num of lower case letters:",count)
#EG:2
s1='restarter'
s1='IMAGINE'
fst=s1[0]
bal=s1[1:]
txt=bal.replace(fst,"$")
print(fst+txt)
#eg:3
s1="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
characters= len(s1)
print(characters)
words=s1.split(" ")
print(words)
'''
print(len(words))
sentences = s1.split('.')
for val in sentences:
    if val =='':
        index = sentences.index('')
        sentences.pop(index)
print(len(sentences))
space = 0
for val in s1:
    if val ==" ":
        space=space+1
print(space)





































