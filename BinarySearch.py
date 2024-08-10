def binary_search(arr, target):
    left = 0 
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            left = mid + 1  # Search the right half
        else:
            right = mid - 1  # Search the left half
    
    return -1 

# user input 
n = int(input("Enter size of array: "))
arr = []
print("Enter elements of array:")
for i in range(n):
    element = int(input())
    arr.append(element)

target = int(input("Enter key to find in the array: "))

result = binary_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
