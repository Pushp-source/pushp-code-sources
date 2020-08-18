a =  (input().split())
b = input().split()
n = int (a[0])
k = int (b[0])
a.remove(a[0])
b.remove(b[0])

str1 = str()
for i in range(k):
    flag = -1
    for j in range (n):
        if (int (b[i]) == int (a[j])):
            flag = j
            break
    print (flag , end= " ")  
def binary_search (lst1,lst2, ln1, ln2, key):
    mid = 
    
    
