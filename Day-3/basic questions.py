'''a=int(input())
sum=0
for i in range(1,a+1):
    sum+=i
print(sum)'''

#===SWAPPING===
'''a=5
b=15
while b!=0:
    a,b=b,a%b
    break
print(a,b)'''

#====GCD===
'''a=21
b=14
while b!=0:
    a,b=b,a%b
print("GCD is:",a)'''

#====LCM====
'''x=int(input())
y=int(input())
product=x*y
gcd=0
while y!=0:
    x,y=y,x%y
    gcd=x
print("gcd is:",x)
print("lcm is:",product//gcd)'''

#====PRIME or not===
'''n=7
fact=0
for i in range(2,int(n**(0.5))+1):
    if n%i==0:
     fact+=1
     break
if fact>=1:
     print("not prime")
else:
     print("prime")'''

#===write a program to print all the prime numbers in a given range===
'''n=int(input())
x=int(input())
fact=0
for i in range(n,x+1):
    for j in range(2,i):
      if i%j==0:
       break
    else:
      print(i,end=" ")'''

#//400 or //4 not 100
year_1=int(input())
year_2=int(input())
leap=0
for i in range(year_1,year_2+1):
     if i%4==0 or i%100!=0:
      leap+=1
      break
     else:
        print(i,"is not a leap year")
print(leap,"is a leap year")
     
    