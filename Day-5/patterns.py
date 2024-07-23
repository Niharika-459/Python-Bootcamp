#  *******
#  *******
#  ******* 
# #print the pattern
'''n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end="")  
    print()'''

n=int(input())
for i in range(n):
    for j in range(n):
        if(i==j):
            print(" ",end="")
        else:
            print("*",end=" ")
    print()

#print upper triangular matrix
#print lower triangle matrix
#print rhombus
#print ***
#       ***
#        ***
#print number pyramid