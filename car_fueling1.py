d = int (input()) # distance between cities
m = int(input()) # miles covered after full tank
n = int (input()) # number of stops
a = input().split() #position of fuel tanks


if (d<=m):
    flag = 0
if (int (a[0]) > m or (d -int( a[n-1]))> m ):
    flag = -1
if (d>m):
    for i in range (n-1):
        if(int(a[i+1]) - int (a[i]) > m):
            flag = -1
else:
    q = int (d/m)
    r = int (d%m)
    if (r== 0):
        flag = q-1
    else:
        flag = q
print (flag)        
  
