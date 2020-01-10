import math
from decimal import Decimal

# odemowanie 1 - sqrt(1 - ( x/2^k )^ 2 ) 
# wygląda następująco:
# od 1 odejmujemy 1 + e
# gdzie |e| > 0 (mała liczba, im większe n tym mniejsza)
# więc im większe n tym bliższym 0 jest wynik odejmowania, 
# wtedy następuje utrata cyfr znaczących,
# a co za tym idzie wyniki mnożeń i pierwiastków są równe 0

# x31 = 0
def x(n):
    x = 2
    for i in range (2, n):
        k = i-1
        x =  pow(2,k) * math.sqrt(2*(1 - math.sqrt(1 - pow(x/pow(2,k), 2)))) 
    return x

def better_x(n):
    x = 2
    for i in range(2, n):
        k = i-1.0
        x = math.sqrt(2)*x/math.sqrt(1 + math.sqrt(1 - pow(x/pow(2,k),2.0))) 
    return x

for i in range(13, 32):
    print("x",i," = ",x(i))

print("\ndalej juz same 0.0, bo: \nsqrt(1 - 0) = 1 \n sqrt(2*(1 - 1)) = 0 \n 2^k * 0 = 0\n\n")

for i in range(1, 1026):
    print("better_x",i," = ",'%.25f'%better_x(i))


print("better_x 1025  = ", '%.25f'%better_x(1025)) # 1026 => Numerical result out of range