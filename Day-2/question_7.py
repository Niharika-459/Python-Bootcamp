#you are given with a comma separated natural numbers 1 to 10.Print only the even numbers
li=list(map(int,input().split(",")))
count=0
for i in range(1,len(li)+1,1):
    if i%2==0:
        count+=1
        print(i)
    else:
        count-=1
    
#----------7.2----------------
print("**count of evens****")
li=list(map(int,input().split(",")))
count=0
for i in range(1,len(li)+1,1):
    if i%2==0:
        count+=1
print(count)

#*******7.3********
# you are given with a space separated integer list find number of even elements and odd 
# elements in a given list
li=list(map(int,input().split(" ")))
even=0
odd=0
for i in range(len(li)):
    if (li[i]%2==0):
        even+=1
    else:
        odd+=1
print("even count=",even,"\nodd count=",odd)



