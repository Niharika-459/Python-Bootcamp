#password verifier=======
#mr.x want to set a new pasword for his instagram account the following conditions should be followed 
#to set the password
#1.password length should be min 8 and max 15
#2.password should have '@' and '/' symbols
#password should contain alphanumeric values
#3.print weak if it has 8 or equal to 8 characters
#else print follow the conditions

'''s=input()
len=len(s)
count=0
str1='@'
str2='/'
for i in(s):
    if i in str1 and i in str2:
     count+=1
     print("strong")
    elif():

            print("follow the conditions")
print("follow the conditions")'''
        

#sort the elements first half in ascending and second half in descending
li=list(map(int,input().split()))
ascending=[]
descending=[] 
li.sort()
print(*li)
n=len(li)
print(n)
for i in range(1,len(li)//2+1):
    ascending.append(li[i])
print(*ascending)
for i in range(len(li)//2+1,-1,-1):
    descending.append(li[i])
print(*descending)
print(ascending+descending)
