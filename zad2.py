r=int(input("введите количество строк(N):"))
c=int(input("введите количество столбцов(m):"))
A=[]
print("Введите элементы массива:")
for i in range(r):
    r_inp= input(f"строка {i+1}:")
    r=list(map(int,r_inp.split()))
    A.append(r)
print("исходный массив A:")
for r in A:
    print(r)
print("-"*40)
#начало задания 11.1
count=0
for i in range(r):
    for j in range(c):
        c_elem=A[i][j]
        n=[]
        for p in range(i-1,i+2):
            for q in range(j-1,j+2):
                if p==i and q==j:
                    continue
                if 0<=p< r and 0<=q<c:
                    n.append(A[p][q])
small=true
if len(n)>0:
    min=min(n)
    if c_elem>=min:
        small=False
if small:
    count+=1
    print(f"Элемент A[{i}][{j}]={c_elem} подходит. его соседи: {n}")
print("-"*40)
print(f"Количество подходящих элементов: {count}")
