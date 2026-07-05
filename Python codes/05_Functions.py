# =====================================
# Question 1: Function with Arguments
# =====================================

def add(a,b):
    return a+b

print(add(10,20))


# =====================================
# Question 2: Function Without Arguments
# =====================================

def greet():
    print("Hello World")

greet()


# =====================================
# Question 3: Lambda Function
# =====================================

add=lambda a,b:a+b

print(add(10,20))


# =====================================
# Question 4: Lambda Function to Find Square
# =====================================

square=lambda n:n*n

print(square(5))


# =====================================
# Question 5: Recursive Factorial
# =====================================

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

print(fact(5))


# =====================================
# Question 6: Recursive Fibonacci
# =====================================

def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)

for i in range(6):
    print(fib(i),end=" ")


# =====================================
# Question 7: Function to Find Maximum
# =====================================

def maximum(a,b):
    if a>b:
        return a
    return b

print(maximum(20,10))


# =====================================
# Question 8: Function to Check Even or Odd
# =====================================

def check(n):
    if n%2==0:
        return "Even"
    return "Odd"

print(check(10))


# =====================================
# Question 9: Function to Find Largest in a List
# =====================================

def largest(arr):
    return max(arr)

print(largest([10,20,5,40,15]))


# =====================================
# Question 10: Function to Reverse a String
# =====================================

def reverse(s):
    return s[::-1]

print(reverse("Python"))