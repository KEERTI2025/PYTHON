# =====================================
# Question 1: Linear Search
# =====================================

arr=[10,20,30,40,50]
key=30

if key in arr:
    print("Found")
else:
    print("Not Found")


# =====================================
# Question 2: Linear Search Without 'in'
# =====================================

arr=[10,20,30,40,50]
key=30
found=False

for num in arr:
    if num==key:
        found=True
        break

if found:
    print("Found")
else:
    print("Not Found")


# =====================================
# Question 3: Binary Search
# =====================================

arr=[10,20,30,40,50]
key=30
low=0
high=len(arr)-1

while low<=high:
    mid=(low+high)//2

    if arr[mid]==key:
        print("Found")
        break
    elif arr[mid]<key:
        low=mid+1
    else:
        high=mid-1


# =====================================
# Question 4: Bubble Sort
# =====================================

arr=[5,3,8,4,2]
n=len(arr)

for i in range(n):
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]

print(arr)


# =====================================
# Question 5: Bubble Sort Using sorted()
# =====================================

arr=[5,3,8,4,2]

print(sorted(arr))