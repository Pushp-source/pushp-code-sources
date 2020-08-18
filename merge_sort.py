def merge_sort(values): 
  
    if len(values)>1: 
        m = len(values)//2
        left = values[:m] 
        right = values[m:] 
        left = merge_sort(left) 
        right = merge_sort(right) 
  
        values =[] 
        k =0
        while len(left)>0 and len(right)>0: 
            if left[0]<right[0]: 
                values.append(left[0]) 
                left.pop(0)
                k = k+1
            else: 
                values.append(right[0]) 
                right.pop(0) 
                k = k+1
        for i in left: 
            values.append(i) 
        for i in right: 
            values.append(i) 
        return k
n = int(input())
lst = input().split()
print(merge_sort(lst))
