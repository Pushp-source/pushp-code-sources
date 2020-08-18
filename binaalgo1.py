
# Python 3 program for recursive binary search. 
# Modifications needed for the older Python 2 are found in comments. 
  
# Returns index of x in arr if present, else -1 
def binary_search(arr, low, high, x): 
  
    # Check base case 
    if high >= low: 
  
        mid = (high + low) // 2
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
  
        # If element is smaller than mid, then it can only 
        # be present in left subarray 
        elif arr[mid] > x: 
            return binary_search(arr, low, mid - 1, x) 
  
        # Else the element can only be present in right subarray 
        else: 
            return binary_search(arr, mid + 1, high, x) 
  
    else: 
        # Element is not present in the array 
        return -1
  
# Test array 
a =  (input().split())
b = input().split()
#if (len(a)>0 and len(b)>0):
n = int (a[0])
k = int (b[0])
#a.remove(a[0])
#b.remove(b[0])    
for i in range(1 ,k+1):
    result = binary_search(a, 1, n, b[i])
    print(result-1 , end = " ")    
  
# Function call 
 
