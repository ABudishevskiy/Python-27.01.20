# 1. дан список [1, 4, 6, 7, 2, 1, 7, 8, 9, 5, 7, 3, 6, 2, 7, 43, 54, 13]
#
#    1.1 найти максимум, минимум и их индексы в массиве
#
#    1.2 найти три самых часто встречаемых элемента массива
#
#    1.3 преобразовать в список где каждое значение будет встречаться только 1 раз
#
#       1.3.1 порядок не сохранялся
#
#       1.3.2 порядок сохранялся
a=[1, 4, 6, 7, 2, 1, 7, 8, 9, 5, 7, 3, 6, 2, 7, 43, 54, 13]
minim=min(a)
maxim=max(a)
indmin=a.index(minim)
indmax=a.index(maxim)
print(minim, maxim, indmin, indmax)

c1=a[0]
c2=a[0]
c3=a[0]
for i in a:
    if a.count(i) >= a.count(c1):
        c1 = i
for i in a:
    if a.count(i) >= a.count(c2) and i != c1:
        c2 = i
for i in a:
    if a.count(i) >= a.count(c3) and i != c2 and i != c1:
        c3 = i
print(c1, c2, c3)

b=set(a)
print(b)
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)