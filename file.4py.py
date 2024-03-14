#DAY:4
#while loop:
# break using while loop
# iterate from 20 to 30 and break the loop in 27
'''
i=20
while i<31:
    if i==27:
        break
    print(i)
    i+=1
i=20
while i<31:
    print(i)
    i+=1
    if i==27:
     break
i=20
while i<31:
  if i==27:
      print(i)
      break
    i+=1
i=20
while i<31:
    if i==27:
        continue
    print(i)
    i+=1
i=20
while i<31:
    i+=1
    if i==27:
        continue
    print(i)
#while to iterate from 12 to 22
i=12
while i<23:    
    print(i)
    i+=1
#find the sum of all numbers
i=12
sum=0
while i<23:
    sum=sum+i
    print(sum)
    i+=1
#1
i=12
sum=0
while i<23:
    sum=sum+i
    i+=1
print(sum)
# find the average of value from 20 to 25
i=20
sum=0
count=0
while i<=30:
    sum=sum+i
    count+=1
    i+=1
    avg= sum/6
print(avg/count)
#NESTED FOR LOOP:
EG:1
for i in range(1,3):
    for j in range(1,4+1):
        print(i,j)
#2
for i in range(4):
    for j in range(4):
        print("*",end=" ")
    print()
#3
rows=8
cols=9
for i in range(rows):
    for j in range(cols):
        print("*",end=" ")
    print()
#4
rows=int(input("enter the rows:"))
cols=int(input("enter the cols:"))
for i in range(rows):
    for j in range(cols):
        print("*",end=" ")
    print()
#5
for row in range(5):
    for col in range(5):
        print(row, end=" ")
    print()
#6
sum = 0
for row in range(5):
    for col in range(5):
        sum= sum+1
        print(sum, end=" ")
    print()
#to print stars in right angle triangel:
for row in range(0,6):
    for col in range(0,row+1):
        print("*",end=" ")
    print()
# to print inverted triangle:
for row in range(0,6):
    for col in range(row+1,6):
        print("*",end=" ")
    print()
#
for row in range(5):
    for col in range(5):
        if col==0 or col==5-1 or row==0 or row==5-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(
#
for row in range(0,5):
    for col in range(0,6):
        if((row==0 and col==3) or (row==1 and (col>=2 and col<4) or (row==2 and (col>=1 and col<=5)))):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#LIST:
#DATA TYPES:
#PRIMARY
# NUMBER
#STRING
#BOOLEAN
#NONE
#COLLECTION
#LIST
#TUPLE
#SET
#DICTIONARY
# list:
#1.if the collection of elements are surounded by square brackets, if is cosidered to be list
#l1=[4,7,99,"hello",7+9j,[8,9,0]]
# characteristics of list
#1.list have ti be surrounded by[]
#2.it is mutable(the elements in the list are changeble)
#3.every element in side the list is indexed
#4.the elements inside list will be ordered format
#5.it can hold duplicate values
#6.itd heterogeneous
#to access the elements in the list
l1=[1,4,1,7,89.7,7,5,"p","i"]
print(l1)
#indexing:
# in the collection datatypes like list,tuple,string the elements will be alloted
#with pre-defined unique value called index value
#we have 2 types of indexing
#1.positive indexing----> starts with zero from left handside
#2.negative indexing----> starts with-1 from roght handside
#POSITIVE INDEXING;
print(l1[4])
#NEGATIVE INDEXING:
l1=[1,4,1,7,89.7,7,5,"p","i"]
print(l1[-4])
#SLICING:
l1=[1,4,1,7,89.7,7,5,"p","i"]
#lst[start index:end index]
print(l1[0:4])
#4
l1=[1,4,1,7,89.7,7.5,"p","i"]
print(l1[6:8])
print(l1[3:6])
print(l1[:5])
print(l1[3:])
print(l1[:])
print(l1[0:7:2])
l1=[1,4,1,7,89.7,7,5,"p","i"]
print(l1[-7:-1:2])
'''
#to insert at add element inside list
l1=[9,8,0,6]
l1.append("car")
print(l1)


    













    
    
      






















 
