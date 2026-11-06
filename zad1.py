def min_max(lst):
    return [min(lst),max(lst)]
numbers= list(map(int,input("Введите числа:").split()))
print("Минимум и Максимум:",min_max(numbers))