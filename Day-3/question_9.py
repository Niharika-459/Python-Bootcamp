#find the elemment present in k+N index
#k=3
#N=2
#input:3 6 8 4 61 2
#output:2
#--------------
#k=3
#n=4
#input:70 54 36 72
#output:error
'''k=int(input())
n=int(input())
li=list(map(int,input().split()))
s=0
#for k in range(len(li)):
s=k+n
print(s)
if(len(li)<=k+n):
    print(error)
else:
    for i in range(len(li)):
      print(li[s])#print(li[5])
      break'''
#cyclic printing#
#print the element in a particular index
#k=8
#80 70 54 36 72
#output:36

k=int(input())
li=list(map(int,input().split()))  #====================
#r=k%len(li)                        k=18
                                    #80 70 54 36 77
idx=k%len(li)         #k%len(li)      1   2  3  4  5
print(idx)      #print(li(i))        #k=18,5 index=3  k%len=remainder
   



