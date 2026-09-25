import math 
x=3.3
num1=math.sin(x)-math.cos(x)
denom1=(1+(x**2)*(math.sin(x)**2))**(1/3)
num2=(x**3)*math.log(x**2)
denom2=math.sin(x)+math.cos(x)
y=(num1/denom1)-(num2/denom2)
print(f"Значение функции при x={x}:y={y}")
