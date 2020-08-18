##def quick_sort(sequence):
##    length = len(sequence)
##    if length <= 1:
##        return sequence
##    else:
##        pivot = sequence.pop()
##        print("pivot is" , pivot)
##    items_greater = []
##    items_lower =[]
##
##    for item in sequence:
##        if item>pivot:
##            items_greater.append(item)
##        else:
##            items_lower.append(item)
##
##    y = quick_sort(items_lower) + [pivot] + quick_sort(items_greater)
##    print (y)
##n = int(input())
##lst = input().split()
##
##x = quick_sort(lst)
##print(x)
##for i in range(n):
##    print(x[i], end = " ")
def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j] <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
n = int (input())
arr = input().split()
quickSort (arr , 0 , n-1)
for i in range(n):
    print(arr[i], end = " ")
    
