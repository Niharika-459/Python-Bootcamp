#take space separated input from user and print alternate elements
#n=100
li=list(map(int,input().split()))
#for i in range(0,n,2):
print(*li[0::2])


li=list(map(int,input().split()))
for i in range(0,len(li),2):
    print(i,end=" ")

