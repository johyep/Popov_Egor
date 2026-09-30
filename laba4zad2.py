import math
proizved=1
for n in range(1,21):
    proizved *= ((2*n**n)-1)/(2*n**n+1)
print("Произведение:",proizved)