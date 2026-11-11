def sort_by_bit(k):
    k.sort(key=lambda x: (bin(x).count('1'), x))
    return k
a = [3, 8, 3, 6, 5, 7, 9, 1]
sort_by_bit(a)
print(a)
  
