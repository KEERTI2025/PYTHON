# =====================================
# Question 1: Reverse a String
# =====================================

s=input("Enter a string: ")
rev=""

for ch in s:
    rev=ch+rev

print(rev)


# =====================================
# Question 2: Reverse a String Using Slicing
# =====================================

s=input("Enter a string: ")
print(s[::-1])


# =====================================
# Question 3: Check Palindrome
# =====================================

s=input("Enter a string: ")
rev=""

for ch in s:
    rev=ch+rev

if s==rev:
    print("Palindrome")
else:
    print("Not Palindrome")


# =====================================
# Question 4: Check Palindrome Using Slicing
# =====================================

s=input("Enter a string: ")

if s==s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# =====================================
# Question 5: Count Vowels
# =====================================

s=input("Enter a string: ").lower()
count=0

for ch in s:
    if ch in "aeiou":
        count+=1

print(count)


# =====================================
# Question 6: Count Uppercase and Lowercase Letters
# =====================================

s=input("Enter a string: ")
upper=0
lower=0

for ch in s:
    if ch.isupper():
        upper+=1
    elif ch.islower():
        lower+=1

print("Uppercase:",upper)
print("Lowercase:",lower)


# =====================================
# Question 7: Remove Spaces
# =====================================

s=input("Enter a string: ")
print(s.replace(" ",""))


# =====================================
# Question 8: Count Words in a String
# =====================================

s=input("Enter a string: ")
print(len(s.split()))


# =====================================
# Question 9: Find Duplicate Characters
# =====================================

s=input("Enter a string: ")
seen=""

for ch in s:
    if s.count(ch)>1 and ch not in seen:
        print(ch,end=" ")
        seen+=ch


# =====================================
# Question 10: Character Frequency
# =====================================

s=input("Enter a string: ")
ch=input("Enter a character: ")
count=0

for i in s:
    if i==ch:
        count+=1

print(count)


# =====================================
# Question 11: Check Anagram
# =====================================

s1=input("Enter first string: ")
s2=input("Enter second string: ")

if sorted(s1)==sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")