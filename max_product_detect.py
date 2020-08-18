


input_n = int(input())
input_numbers = [int(x) for x in input().split()]
max1 = max(input_numbers)
input_numbers1 = input_numbers.remove(max1)
max2 = max(input_numbers)
print ((max1*max2))
