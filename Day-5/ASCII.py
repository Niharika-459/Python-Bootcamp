#sum the digits of a string using ascii values==
'''inp=input()
count=0
for i in(inp):
    if ord(i)>=48 and ord(i)<=57:
        count+=int(i)
print(count)'''

#write a code to print all the capital letters in a given string
'''inp=input()
count=0
r=""
for i in(inp):
    if ord(i)>=65 and ord(i)<=96:
        r+=(i)
print(r)'''

#remove all the braces from the given algebraic expression
'''inp=input()
for i in (inp):
    if(ord(i)==40 or ord(i)==41 or ord(i)==91 or ord(i)==93 or ord(i)==123 or ord(i)==125):
        pass
    else:
       print(i,end=" ")'''
#print the characters after the string
'''li=input()
count=0
for i in li:
    print(chr(ord(i)+4),end=" ")
    #count+=(i)
#print(count))'''
#2nd METHOD





#input==>hello---wor---ld
#output==>------helloworld
'''li=input()
count=0
r=""
for i in li:
    if i=='-':
        count+=1
print(count)
for i in li:
    if ord(i)>=97 and ord(i)<=123:
         r+=i
print('-'*count+r)'''
#another method
'''li=input()
count=0
r=""
for i in li:
    if i=='-':
        count+=1
    else:
     r+=i
print('-'*count+r)'''


