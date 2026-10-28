k_str=input("Введите коэф:")
k=[float(x)for x in k_str.split()]
x=float(input("Введите x:"))
if len(k)<=1:
    print("производная равна:0.0 ")
else:
    mass_k=[]
    for i in range(1,len(k)):
        new_k=k[i]*i
        mass_k.append(new_k)
    res=0
    for i in range(len(mass_k)):
        res+=mass_k[i]*(x**i)
    print(f"Массив коэффициентов производной:{mass_k}")
    print(f"Значение производной в точке {x}: {res}")
