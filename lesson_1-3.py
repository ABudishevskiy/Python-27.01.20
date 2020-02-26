# 3. реализовать разложение числа на степени простых множителей (ввод через input, выход по 0)
#
# (простое число - делится только на себя и 1)
#
# вход:
#
# 456
#
# 0
#
# вывод:
#
# 2^3 * 3 * 19
import sys
while True:
    n=int(input('enter number'))
    if n == 0:
        sys.exit()
    a = {}
    i = 2
    while n != 1:
        if n % i == 0:
            n = n // i
            a[i]=a.get(i, 0)+1
            continue
        i+=1
    print(a)