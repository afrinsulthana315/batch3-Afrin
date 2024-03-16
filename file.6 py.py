#DAY:6
#python program to capitalize the first and last character of each
'''
s1='hello world'
fst=s1[0].upper()
lst=s1[-1].upper()
print(fst+s1[1:len(s1)-1]+lst)
#2.
n=128
temp=n
str1=''
f1=0
while n!=0:
    rem=n%10
    check=temp%rem
    if check!=0:
        f1 = 1
        n=n/10
    if f1 ==0:
             print("yes")
    else:
        print("no")
#3:
l1=[1,3,15,28]
l2=[7,8,5,45]
l3=[]
for val in range(len(l1)):
    ans= l1[val]+l2[val]
    l3.append(ans)
    print(l3)
#set
#characteristic of set
#1.set can be created using{}
#2.the element inside set are not indexed
#3.does not allow duplicate value
#4.it unordered
#5.heterogenoud
#6.mutable or changeable
#EG:1
s1={9,9,89,7.76,8+7j,(8,7,5),"truck",'e'}
print(s1)
#EG:2
#error coz accept only unmutable data types
s2={2,98,5,[3,15]}
print(s2)
#EG:3
#to add element inside set
s1={8,78,67,'u'}
s1.add(43)
print(s1)
s1.update([9,0])
print(s1)
# to delete element iside the set
# pop--->to delete one element randomly
s1={8,78,67,'u'}
s1.pop()
print(s1)

#remove
s1={8,78,67,'u'}
s1.remove(78)
print(s1)

#discard
s1={8,78,67,'u'}
s1.discard(67)
print(s1)

#clear
datatype id dictionary
l1={}
print(type(l1))

#delete
#error
s1={8,78,67,'u'}
del s1
print(s1)

#join the sets
s1={9,0,8}
s2={9.90,'card','t',56}

#union-->to combine 2 sets
s3=s1.union(s2)
print(s3)

#intersection()-->to get common element inside set
s1={4,5,6}
s2={5,6,7,8}
print(s1.intersection(s2))
#
s1={4,5,6}
s2={5,6,7,8}
print(s1.difference(s2))
print(s2.difference(s1))
print(s1.symmetric_difference(s2))
#
s1={8,9,0}
s2={6,7,5,8,9,0}
print(s1.issubset(s2))
print(s2.issubset(s1))

#o/p --->its a joinset
s1={1,2,3,4,5}
s2={3,2,7,8,9}
for val in s1:
    if val in s2:
        str1="its joint set"
print(str1)

#---->dictionary
#EG:1
d1={1:100,'a':200,5.4:"hello"}
print(d1)
print(len(d1))
#characteristics of dictionary
#1.have to be surrounded by{}
#2. it have to be in the form of key,value pair
#3.it is mutable
#4.duplicate keys are not allowed'duplicate values are allowed
#5.it is ordered
#6.key does not allow mutable datatypes,value allow mutable datatype

d1={1:100,2:200,3:300,4:400}
print(d1)
#to access the values,hav eto use key
print(d1[1])
# some coomon functions
# len(),min(),max()
d1={1:100,2:200,3:300,4:400}
print(min(d1))
print(max(d1))
# to find min,max based on values
print(min(d1.values()))
print(max(d1.values()))
# dictionary based functions
#to add element(key and value pair)in dict
d1={1:100,2:200,3:300,4:400}
d1[5]=500
print(d1)
# to replace a value in dictionary
d1={1:100,2:200,3:300,4:400}
d1[2]="mango"
print(d1)
#delete element from dictionary
d1={1:100,2:200,3:300,4:400}
#pop item()
d1.popitem()
print(d1)
#
d1={1:100,2:200,3:300,4:400}
print(d1.popitem())
#pop
# 2 is the key in dictionary
d1={1:100,2:200,3:300,4:400}
d1.pop(2)
print(d1)

#join 2 dict
d1={1:100,2:200,3:300,4:400}
d2={"a":"apple","b":"boy","g":"girl"}
d1.update(d2)
print(d1)

#get()-->used to get a value from key
d1={1:100,2:200,3:300,4:400}
#error
#print(d1[90])
print(d1.get(90))

# to pirnt all the keys
d1={1:100,2:200,3:300,4:400}
print(d1.keys())
print(type(d1.keys()))

# to print the values
d1={1:100,2:200,3:300,4:400}
print(d1.values())

# iterating dictionary
# to iterate keys alone'
d1={1:100,2:200,3:300,4:400}
for val in d1:
    print(val)
# to iterate value alone
for val in d1.values():
    print(val)
#to get both key and values
for key,val in d1.items():
    print(key,val)

# 1.
n=int(input("enter number of times:"))
integer=[]
float=[]
string=[]
for val in range(n):
    value=eval(input("enter the values:"))
    if type(value)==int:
        integer.append(value)
    elif type(value)==float:
        float_value.append(value)
    elif type(value)==str:
        string.append(value)
    else:
        print(" pls provide the data of int,float_val,string")
print(integer)
print(float_value)
print(string)

# return a set of elements present in setA or B but not both
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3=set()
for val in set1:
    if val not in set2:
        set3.add (val)
for val in set2:
    if val not in set1:
        set3.add(val)
print(set3)

#3
l1=[1,2,3,4]
l2=['a','b','c','d',]
d1={}
d1[l1[0]] =l2[0]
print(d1)
'''
#4
l1=[1,2,3,4]
l2=['a','b','c','d',]
d1={}
for val in range(len(l1)):
    d1[l1[val]] = l2[val]
print(d1)


























