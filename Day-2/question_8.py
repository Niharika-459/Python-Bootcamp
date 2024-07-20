#given an space separated integer list find the average of elements in the even index
li=list(map(int,input().split(" ")))
sum=0
even=0
n=len(li)
for i in range(len(li)):
    if i%2==0:
        sum+=li[i]
        even+=1
print(sum/even)



