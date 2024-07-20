#prime or not
import math
n=int(input())
for i in range(2,int(math.sqrt(n)+1),1):
    if n%i==0:
         print("not prime")
         exit(0)
    else:
       print("prime")
       exit(0)

#2 method
'''
n=int(input())
fact=0
if n<1:
    print("neither prime nor composite")
for i in range(2,n//2,n-1):
    if(n%i==0):
        fact+=1
        print("prime")
        exit(0)
    else:
        print("not a prime")
        exit(0)'''


#***************************PALINDROME******************************************#
#num=int(input())
#rem=0
#res=0
#temp=num
#while(num>0):
#    rem=num%10     
#   res=(res*10)+rem       
#   num=num//10
#if res==temp:
#          print("palindrome")
#else:
#     print("not a palindrome")


#*****************ARMSTRONG***********
'''arm=int(input())
sum=0
copy_arm=arm
no_of_digits=len(str(arm))
while(arm>0):
    digit1=arm%10
    sum+=digit1**no_of_digits
    arm=arm//10
if sum==copy_arm:
    print(copy_arm,"is an armstrong number")
else:
    print(copy_arm,"is not an armstrong number")'''



#*********SUM OF NATURAL NUMBERS***********
'''n=int(input())
for i in range(n):
    res=(n*(n+1)//2)
print(res)
'''

'''
******************FRIENDLY NUMBER***************

a=int(input())
b=int(input())
fact1=0
sum1=0
fact2=0
sum2=0
for i in range(1,a-1):
     if a//i==0:     
            fact1+=1
            sum1=sum1+i
     for j in range(1,b-1):
         if b//j==0:
                 
                fact2+=1
                sum2=sum2+j
if sum1==b and sum2==a:
            print(a,b,"are friendly numbers")
else:
            print(a,b,"are not friendly numbers")'''
