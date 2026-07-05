# =====================================
# Question 1: Right Triangle Star Pattern
# =====================================

n=5

for i in range(1,n+1):
    print("*"*i)


# =====================================
# Question 2: Inverted Right Triangle Pattern
# =====================================

n=5

for i in range(n,0,-1):
    print("*"*i)


# =====================================
# Question 3: Pyramid Star Pattern
# =====================================

n=5

for i in range(n):
    print(" "*(n-i-1)+"*"*(2*i+1))


# =====================================
# Question 4: Inverted Pyramid Pattern
# =====================================

n=5

for i in range(n):
    print(" "*i+"*"*(2*(n-i)-1))


# =====================================
# Question 5: Diamond Pattern
# =====================================

n=5

for i in range(n):
    print(" "*(n-i-1)+"*"*(2*i+1))

for i in range(n-2,-1,-1):
    print(" "*(n-i-1)+"*"*(2*i+1))


# =====================================
# Question 6: Number Triangle Pattern
# =====================================

n=5

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()


# =====================================
# Question 7: Floyd's Triangle
# =====================================

n=4
num=1

for i in range(1,n+1):
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()


# =====================================
# Question 8: Pascal's Triangle
# =====================================

n=5

for i in range(n):
    num=1
    print(" "*(n-i),end="")
    for j in range(i+1):
        print(num,end=" ")
        num=num*(i-j)//(j+1)
    print()


# =====================================
# Question 9: Alphabet Triangle Pattern
# =====================================

n=5

for i in range(1,n+1):
    for j in range(i):
        print(chr(65+j),end="")
    print()


# =====================================
# Question 10: Hollow Square Pattern
# =====================================

n=5

for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


# =====================================
# Question 11: Hollow Rectangle Pattern
# =====================================

r=4
c=6

for i in range(r):
    for j in range(c):
        if i==0 or i==r-1 or j==0 or j==c-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()