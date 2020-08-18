length = int (input())
summ = 0
a =input().split()
b= input().split()
A = list()
B = list()
for i in range(length):
    A.append(int (a[i]))
    B.append(int (b[i]))
A.sort(reverse = True)
B.sort(reverse = True)
for j in range(length):
    summ = summ + int(A[j])*int (B[j])
print (summ)


