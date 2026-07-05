# =====================================
# Question 1: Multiplication Table
# =====================================

n=5

for i in range(1,11):
    print(n,"x",i,"=",n*i)


# =====================================
# Question 2: Sum of First N Numbers
# =====================================

n=5
total=0

for i in range(1,n+1):
    total+=i

print(total)


# =====================================
# Question 3: Factorial
# =====================================

n=5
fact=1

for i in range(1,n+1):
    fact*=i

print(fact)


# =====================================
# Question 4: Prime Number
# =====================================

n=7
count=0

for i in range(1,n+1):
    if n%i==0:
        count+=1

if count==2:
    print("Prime")
else:
    print("Not Prime")


# =====================================
# Question 5: Armstrong Number
# =====================================

n=153
total=sum(int(i)**3 for i in str(n))

if total==n:
    print("Armstrong")
else:
    print("Not Armstrong")


# =====================================
# Question 6: Fibonacci Series
# =====================================

n=5
a=0
b=1

for i in range(n):
    print(a,end=" ")
    a,b=b,a+b


# =====================================
# Question 7: GCD
# =====================================

import math

print(math.gcd(12,18))


# =====================================
# Question 8: LCM
# =====================================

import math

a=12
b=18

print((a*b)//math.gcd(a,b))


# =====================================
# Question 9: Perfect Number
# =====================================

n=28
total=0

for i in range(1,n):
    if n%i==0:
        total+=i

if total==n:
    print("Perfect Number")
else:
    print("Not Perfect Number")


# =====================================
# Question 10: Count Digits
# =====================================

n=12345

print(len(str(n)))


# =====================================
# Question 11: Sum of Digits
# =====================================

n=1234
total=0

for digit in str(n):
    total+=int(digit)

print(total)