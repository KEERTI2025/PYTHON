# =====================================
# Question 1: Count Frequency Using Dictionary
# =====================================

arr=[1,2,2,3,2,4]
freq={}

for num in arr:
    freq[num]=freq.get(num,0)+1

print(freq)


# =====================================
# Question 2: Count Frequency Using count()
# =====================================

arr=[1,2,2,3,2,4]

for num in set(arr):
    print(num,":",arr.count(num))


# =====================================
# Question 3: Dictionary Key-Value Swap
# =====================================

d={"a":1,"b":2,"c":3}
new={}

for key,value in d.items():
    new[value]=key

print(new)


# =====================================
# Question 4: Dictionary Key-Value Swap Using Comprehension
# =====================================

d={"a":1,"b":2,"c":3}
new={value:key for key,value in d.items()}

print(new)


# =====================================
# Question 5: Sort a Dictionary by Value
# =====================================

d={"a":30,"b":10,"c":20}

for key,value in sorted(d.items(),key=lambda x:x[1]):
    print(key,value)


# =====================================
# Question 6: Set Union
# =====================================

a={1,2,3}
b={3,4,5}

print(a|b)


# =====================================
# Question 7: Set Intersection
# =====================================

a={1,2,3}
b={3,4,5}

print(a&b)


# =====================================
# Question 8: Set Difference
# =====================================

a={1,2,3}
b={3,4,5}

print(a-b)


# =====================================
# Question 9: Convert List to Tuple
# =====================================

arr=[10,20,30,40]

t=tuple(arr)

print(t)


# =====================================
# Question 10: Convert Tuple to List
# =====================================

t=(10,20,30,40)

arr=list(t)

print(arr)


# =====================================
# Question 11: Find Unique Elements
# =====================================

arr=[10,20,10,30,20,40]

print(set(arr))


# =====================================
# Question 12: Find Unique Elements as List
# =====================================

arr=[10,20,10,30,20,40]

print(list(set(arr)))