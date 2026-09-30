import math
sm=0
x=math.pi/3
for n in range(1,51):
    sm += ((x**(2*n+1))/math.factorial(2*n+1))
print("Сумма:",sm)
