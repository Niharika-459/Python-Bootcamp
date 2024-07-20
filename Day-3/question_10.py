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

#find the duplicatres in an array
'''original=list(map(int,input().split()))
li=[]
for i in original:
    if(i not in li):
        li.append(i)
print(*li)'''

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
num=int(input())
rev=""
while num>0:
    r=num%10 
    rev=rev+str(r)
    num=num//10
print(int(rev))


#sum of squares of given number
#find sum of squares of even and odd digits
#check whether given number is palindrome or not using while
#write a program to print first n fibonacci series