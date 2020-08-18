d = int (input())
m = int(input())
n1 = m
n = int (input())
x = input().split()
lst1 = list() 
count = 0
for i in range(n-1): 
    if (int(x[0])> m or (d - int(x[n-1])) > m ):
       flag = -1
       break
    elif(d<=m):
        flag = 0
        break
    elif (int(x[i+1]) - int (x[i]) > m):
       flag = -1
       break
    else:
       count = int (d/m)
       r = int (d%m)
       if (r==0):
           count = count-1
           flag = count
       if(r>0):
           flag = count
print (flag)       
        
