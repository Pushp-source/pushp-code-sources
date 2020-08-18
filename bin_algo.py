import math
def bin_search (A ,low, high, key):
    if (high<low):
        return 0
##    if (len(A)==0):
##        return 0
    mid = math.floor(low+ ((high-low)/2))
    if (key == int (A[mid])):
        return mid 
    if (key <int (A[mid])):
        return bin_search(A,low, mid-1, key)
    if (key>int (A[mid])):
        return bin_search(A, mid+1, high, key)
a =  (input().split())
b = input().split()
#if (len(a)>0 and len(b)>0):
n = int (a[0])
k = int (b[0])
#a.remove(a[0])
#b.remove(b[0])    
for i in range(1 ,k+1):
    index = bin_search(a,1,n,int (b[i]))
    print(index-1 , end = " ")    
#else:
    #print(-1)
