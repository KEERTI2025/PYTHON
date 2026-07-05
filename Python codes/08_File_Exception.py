# =====================================
# Question 1: Read a File
# =====================================

file=open("demo.txt","r")
print(file.read())
file.close()


# =====================================
# Question 2: Write to a File
# =====================================

file=open("demo.txt","w")
file.write("Hello World")
file.close()


# =====================================
# Question 3: Append to a File
# =====================================

file=open("demo.txt","a")
file.write("\nWelcome to Python")
file.close()


# =====================================
# Question 4: Read a File Using with
# =====================================

with open("demo.txt","r") as file:
    print(file.read())


# =====================================
# Question 5: Try-Except Example
# =====================================

try:
    a=10
    b=0
    print(a/b)
except:
    print("Cannot divide by zero")


# =====================================
# Question 6: Try-Except-Else-Finally
# =====================================

try:
    a=10
    b=2
    print(a/b)
except:
    print("Error")
else:
    print("No Error")
finally:
    print("Program Finished")