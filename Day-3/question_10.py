#find the maximum element in a given list
'''li=list(map(int,input().split()))
print(max(li))'''
'''max=0
li=list(map(int,input().split()))
for i in range(0,len(li)):    #max=li[0]
    for j in range(1,len(li)):#for i in range(li)
        if(li[i]<li[j]):      #if(li>max)
         max=li[j]            #max=li[i]
print(max)                    #print(max)'''


#find min element
'''li=list(map(int,input().split()))
min=li[0]
for i in range(len(li)):
    if(li[i]<min):
        min=li[i]
print(min)'''


#replace the elements in an array  with average of max an min element
#13 2 67 20 68
#max=68,min-2
#avg=35
#output=35 35 35 35 35
'''li=list(map(int,input().split()))
max=li[0]
min=li[0]
s=0
t=0
for i in range(len(li)):
    if(li[i]<min):
        min=(li[i])
        print(min)
    elif(li[i]>max):
        max=(li[i])
print(max)
#print((max+min)//2)'''

'''li=list(map(int,input().split()))
min=li[0]
for i in range(len(li)):
    if(li[i]<min):
        min=li[i]
print(min)
max=li[0]
for i in range(len(li)):
    if(li[i]>max):
        max=li[i]
print(max)
avg=(min+max)//2
print(avg)
for i in range(len(li)):
    li[i]=avg
print(li)'''



#find the missing number in an array
'''li=list(map(int,input().split()))
sum=0
x=int(input())
for i in range(0,len(li)):
    sum+=li[i]
    t=(x*(x+1))//2
#print(x)
#print(t)
print(sum)
print(t-sum)'''

#find the duplicates in an array
original=list(map(int,input().split()))
li=[]
for i in original:
    if(i not in li):
        li.append(i)
print(*li)

#find unique values
'''li=list(map(int,input().split()))
dup=[]
count=0
for i in li:
    count+=1
    if count>=2:
       dup.append(i)
print(*dup)'''


#sum of digits-->123-->1+2+3=6
'''num=int(input())
sum=0
while num>0:
    r=num%10     
    sum=sum+r       
    num=num//10
print(r)
print(sum)'''
#print(res)

#sum of even digits
'''num=int(input())
sum=0
while num>0:
    r=num%10 
    if r%2==0:    
     sum=sum+r       
    num=num//10
print(sum)'''

#print reverse of a number-->123-->321
'''num=int(input())
rev=""
while num>0:
    r=num%10 
    rev=rev+str(r)
    num=num//10
print(int(rev))'''


#sum of squares of given number
'''num=int(input())
sum=0
while num>0:
    r=num%10     
    sum=sum+r**2      
    num=num//10
print(sum)'''
#******find sum of squares of even and odd digits********
'''num=int(input())
even_sum=0
odd_sum=0
while num>0:
    r=num%10
    num=num//10
    if r%2==0:
        even_sum=even_sum+r**2
    else:
       odd_sum=odd_sum+r**2
print(even_sum,odd_sum)'''
    
#check whether given number is palindrome or not using while
'''num=int(input())
copy=num
rev=""
while num>0:
    r=num%10 
    rev=rev+str(r)
    num=num//10
if copy==int(rev):
    print("palindrome")
else:
    print("not a palindrome")
print(int(rev))
#print(copy)
#print(num)'''

#write a program to print first n fibonacci series
'''n=int(input())
a,b=0,1
while b<=n:
    print(b)
    a,b=b,a+b'''

#find max element in array
'''li=list(map(int,input().split()))
max=li[0]
for i in range(len(li)):
    if li[i]>max:
     max=li[i]
print(max)'''

#=========FIND SECOND MAX ELEMENT IN AN ARRAY==========
'''li=list(map(int,input().split()))
first_max=li[0]
second_max=li[1]
for i in range(len(li)):
   if li[i]>first_max:
      second_max=first_max
      first_max=li[i]
   elif li[i]>second_max:
      second_max=li[i]
print(second_max)'''

#====REVERSE OF AN ARRAY WITHOUT INBUILT FUNCTIONS=====
'''li=list(map(int,input().split()))
reverse=[]
print(len(li))
for i in(len(li)-2,len(li)):
     reverse.append(i)
print(*reverse)'''

#===PEEK ELEMENT=====
#5 *****
'''li=list(map(int,input().split()))
peek=0
for i in range(1,len(li)-1):
    if li[i]>li[i-1] and li[i]>li[i+1]:
     peek+=1#-->count of peek elements
     #break-->only first peek element
print(li[peek])#printing all peek elements'''

#method-2

li=list(map(int,input().split()))
peek=0
for i in range(1,len(li)-1):
    if li[i]>li[i-1] and li[i]>li[i+1]:
       peek=i
if li[-1]>li[-2] and li[-1]>peek:
     peek=len(li)-1#-->count of peek elements
     #break-->only first peek element
print(li[peek])#printing all peek elements
