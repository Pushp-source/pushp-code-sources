#money_change
m = int (input())
count1 =int( m/10)
count2 =int(((m%10))/5)
count3 = (m%10)%5
total = count1+count2+count3
print (total)
