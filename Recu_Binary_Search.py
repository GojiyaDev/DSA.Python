def binary_search(arr, target):
    def binary_search_recursive(arr, target, left, right):
        if left <= right:
            mid = (left + right) // 2
            
            if arr[mid] == target:
                return mid  
            elif arr[mid] < target:
                return binary_search_recursive(arr, target, mid + 1, right) 
            else:
                return binary_search_recursive(arr, target, left, mid - 1)  
        else:
            return -1      
    
    return binary_search_recursive(arr, target, 0, len(arr) - 1)

# Take user input for array size
n = int(input("Enter the size of the array: "))

# Take user input for array elements
arr = []
print("Enter the elements of the array:")
for i in range(n):
    arr.append(int(input()))

target = int(input("Enter the element to search for: "))
result = binary_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
