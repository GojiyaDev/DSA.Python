def find_max_min(arr):
    #if array is not avaiable
    if not arr:
        return None, None
    max_elem = arr[0]
    min_elem = arr[0]

    #check through loop
    for num in arr:
        #check for Largest value in array
        if num > max_elem:
            max_elem = num
        #check for smallest value in array
        if num < min_elem:
            min_elem = num
    return max_elem, min_elem

# Elements for Search Max and Min
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
max_elem, min_elem = find_max_min(arr)
print("Maximum element: ",max_elem)
print("Minimum element: ",min_elem)

