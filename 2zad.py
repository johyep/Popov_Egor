import math
a, b, h = 0.1, 0.7, 0.05
print(f"{"x":>6} {"y":>10}")
print("-"*19)
x=a
while x <=b + 1e-9:
    num=(x**math.sin(x)) + (math.sin(x)**x)
    den=x**abs(math.cos(2*x)) + math.cos(x)**(2*x)
    y=num/den
    print(f"{x:6.2f} {y:10.6f}")
    x+=h