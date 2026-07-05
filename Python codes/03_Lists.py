# =====================================
# Question 1: Find Largest Element
# =====================================

arr=[10,20,5,40,15]
print(max(arr))


# =====================================
# Question 2: Find Largest Element Without max()
# =====================================

arr=[10,20,5,40,15]
largest=arr[0]

for num in arr:
    if num>largest:
        largest=num

print(largest)


# =====================================
# Question 3: Find Smallest Element
# =====================================

arr=[10,20,5,40,15]
print(min(arr))


# =====================================
# Question 4: Find Smallest Element Without min()
# =====================================

arr=[10,20,5,40,15]
smallest=arr[0]

for num in arr:
    if num<smallest:
        smallest=num

print(smallest)


# =====================================
# Question 5: Find Second Largest Element
# =====================================

arr=[10,20,5,40,15]
arr.sort()
print(arr[-2])


# =====================================
# Question 6: Find Largest and Second Largest
# =====================================

arr=[10,20,5,40,15]
largest=arr[0]
second=arr[0]

for num in arr:
    if num>largest:
        second=largest
        largest=num
    elif num>second and num!=largest:
        second=num

print("Largest:",largest)
print("Second Largest:",second)


# =====================================
# Question 7: Find Sum of Array Elements
# =====================================

arr=[1,2,3,4,5]
print(sum(arr))


# =====================================
# Question 8: Find Sum Without sum()
# =====================================

arr=[1,2,3,4,5]
total=0

for num in arr:
    total+=num

print(total)


# =====================================
# Question 9: Remove Duplicates from a List
# =====================================

arr=[10,20,10,30,20,40,50,40]
print(list(set(arr)))


# =====================================
# Question 10: Remove Duplicates Without set()
# =====================================

arr=[10,20,10,30,20,40,50,40]
new=[]

for num in arr:
    if num not in new:
        new.append(num)

print(new)


# =====================================
# Question 11: Reverse a List
# =====================================

arr=[1,2,3,4,5]
print(arr[::-1])


# =====================================
# Question 12: Reverse a List Using reverse()
# =====================================

arr=[1,2,3,4,5]
arr.reverse()
print(arr)


# =====================================
# Question 13: Sort a List
# =====================================

arr=[4,2,5,1,3]
arr.sort()
print(arr)


# =====================================
# Question 14: Sort a List Using sorted()
# =====================================

arr=[4,2,5,1,3]
print(sorted(arr))


# =====================================
# Question 15: Merge Two Lists
# =====================================

a=[1,2,3]
b=[4,5,6]
print(a+b)


# =====================================
# Question 16: Merge Two Lists Using extend()
# =====================================

a=[1,2,3]
b=[4,5,6]
a.extend(b)
print(a)


# =====================================
# Question 17: Find Intersection of Two Lists
# =====================================

a=[1,2,3,4]
b=[3,4,5,6]
print(list(set(a)&set(b)))


# =====================================
# Question 18: Find Intersection Without set()
# =====================================

a=[1,2,3,4]
b=[3,4,5,6]
c=[]

for num in a:
    if num in b:
        c.append(num)

print(c)


# =====================================
# Question 19: Find Minimum and Maximum Elements
# =====================================

arr=[10,20,5,40,15]
print("Minimum:",min(arr))
print("Maximum:",max(arr))


# =====================================
# Question 20: Find Minimum and Maximum Without Built-in Functions
# =====================================

arr=[10,20,5,40,15]
minimum=arr[0]
maximum=arr[0]

for num in arr:
    if num<minimum:
        minimum=num
    if num>maximum:
        maximum=num

print("Minimum:",minimum)
print("Maximum:",maximum)


# =====================================
# Question 21: Find Missing Number in a List
# =====================================

arr=[1,2,3,5]

for num in range(1,6):
    if num not in arr:
        print(num)


# =====================================
# Question 22: Find Duplicates in a List
# =====================================

arr=[10,20,10,30,20,40]
dup=[]

for num in arr:
    if arr.count(num)>1 and num not in dup:
        dup.append(num)

print(dup)


# =====================================
# Question 23: Find the Most Frequent Element
# =====================================

arr=[1,2,2,3,2,4]
print(max(arr,key=arr.count))