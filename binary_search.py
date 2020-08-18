a =  (input().split())
b = input().split()
l = int (a[0])
a.remove(a[0])
b.remove(b[0])

str1 = str()
for i in range(l):
    flag = -1
    for j in range (l):
        if (int (b[i]) == int (a[j])):
            flag = j
            break
    print (flag , end= " ")  
