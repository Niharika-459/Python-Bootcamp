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