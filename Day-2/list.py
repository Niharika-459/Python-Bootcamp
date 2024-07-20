'''my_list=[1,-2,2,3,4,5,-9,87,-54]
my_list.append(888)
my_list.insert(0,987)
print(len(my_list))
my_list.pop()#last element is popped
li2=[8,9,10]
li2.pop(1)# 1 index element is popped
li3=my_list.copy()
cnt=my_list.count(2)#counts the number of times the elemrnt is repreatingS
print(cnt)
print(*my_list)
print(*my_list+li2)
print(*li3)
#sort function-->quick sort-->timecomplexity(nlogn)
my_list.sort()
print(*my_list)'''

'''li=list(map(int,input().split(",")))
print(*li)
li=list(map(str,input().split(",")))
print(*li)'''

#1--append  2--pop 3--sort 4--len

'''li=list(map(int,input().split()))
print("*******\n1-append\n2-pop\n3-sort\n4-length of list\n*****")
print("enter choice:")
choice=int(input())
if choice==1:
    li.append(23)
    print(*li)
elif choice==2:
    li.pop()
    print(*li)
elif choice==3:
    li.sort()
    print(*li)
elif choice==4:
    print(len(li))
else:
    print("invalid choice")'''


