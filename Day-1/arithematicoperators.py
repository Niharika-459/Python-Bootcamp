a=int(input())
b=int(input())
print(f"{a+b}\n {a-b}\n {a*b}\n {a/b}\n {a**b}\n {a//b}\n")
#pow-->import math module-->**-->pow(a)
#logical operators-->&&(and),or(||)
age=int(input())
if age>=18 and age<24:
    print("only two wheeler")
elif(age>=24 and age<45):
    print("both two and four wheeler")
else:
    print("two wheeler,four wheeler and six")
#print("//*****************//")
m=700
apples=int(input())
bananas=int(input())
oranges=int(input())
sum=apples*15+bananas*12*4+oranges*5
print(sum)
if sum<=m:
    print("not been cheated")
else:
    print("been cheated")
#print("//*********//")

a=int(input())
if(a>0 and a%2==0):
    print("positive and even")
elif(a>0 and a%2!=0):
    print("positive and odd")
elif(a<0 and a%2==0):
    print("negative and even")
else:
    print("negative and odd")




#Mr.Z is selected for olympics he is participating in swimming competition only one winner is 
# selected among all partcipants mr.z got selected,mr.x and mr.y are friends of mr.z mr.x is 
# participating in badminton 
# mr.y is participating in table tennis according to selection commitee the requirements for 
# badminton players are
#1.height-->140cm
#2.weight-->factors of 2
#3.body fat-->less than 12%
#according to the selection commitee requirements for table tennis are
#1.height-->min 118cm to 148cm
#2.weight-->factors of no.of medals won by mr.z
#3.body fat-->14%
#according to the previous history Z participated in 14 games out of which he is having success 
#rate of 50%.
#write a program to check whether mr.x,mr.y,mr.z from india travel in a same plane or not
#

h_x=int(input())
w_x=int(input())
h_y=int(input())
w_y=int(input())
count=0
if h_x==140 and w_x%2==0 :
    count+=1
    print("x selected")
elif(h_y in range(118,148) and w_y%7==0):
    count+=1
    print("y selected")
elif count==2:
    print("they travel in same flight ")
else:
    print("they not  travel in same flight ")
