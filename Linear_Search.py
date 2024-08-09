n = int(input("Enter Size of Element: "))
arr = []

print("Enter Elements :")
for i in range(n):
    element = int(input())
    arr.append(element)

print("Array From Input :", arr)

key = int(input("Enter Key : "))

for i in range(len(arr)):
    if arr[i] == key:
        count = 1  
        break      
    else:
        count = -1
    
if(count >= 1):
    print("Index of Array Where is Element : ",i)
else:
    print("Not Found")
