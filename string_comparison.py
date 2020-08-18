a = input()#azced
b = input() #abcdef
f =list(a)
f.insert(0, '0')
g = list(b)
g.insert(0,'0')
#print(g)
#b.split()
#print(b)
##lst1 =[]
##lst2 = []
mind = []
n1 =len(f)
n2 =len(g)
##for x in range(n1):
##    lst1.append(a[x])
##print(lst1)    
##    
##for y in range(n2):
##    lst2.append(b[y])
##print(lst2)
    
for i in range(n1):
    mind.append([])#create an smpty sublist inside list
    mind[i].append(i)
    for j in range(1,n2):
         if(i==0):
             mind[i].append(j)
         else:
             if(f[i]==g[j] ):
                 x = mind[i-1][j-1]
             else:
                 x = min(mind[i][j-1],mind[i-1][j-1], mind[i-1][j])+1
             mind[i].append(x)
#print(mind)
h =[]
for w in mind:
     h.append(w[n2-1])
#print(h)

#print(h)
#print(min(h))     
print(mind[n1-1][n2-1])    
        
