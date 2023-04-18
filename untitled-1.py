n = int(input())
l = list()
for i in range(n):
    l0 = list(map(int, input().split()))
    if l0[0] % 2 != 0:
        l.append(l0)
#первое число макс второе мин
l1 = list() #нн
a1 = 10**9
l2 = list() #нч
a2 = 10**9
l3 = list() #чн
a3 = 10**9
s1 = 0
s2 = 0
n = len(l)
for i in range(n):
    if max(l[i]) % 2 != 0 and min(l[i]) % 2 != 0 and sum(l[i]) < a1:
        l1 = l[i]
        a1 = sum(l[i])
    elif max(l[i]) % 2 != 0 and min(l[i]) % 2 == 0 and sum(l[i]) < a2:
        l2 = l[i]
        a2 = sum(l[i])
    elif max(l[i]) % 2 == 0 and min(l[i]) % 2 != 0 and sum(l[i]) < a3:
        l3 = l[i]
        a3 = sum(l[i])
    s1 += max(l[i])
    s2 += min(l[i])
if s1 % 2 != 0 and s2 % 2 == 0:
    print(s1 + s2)
elif s1 % 2 == 0 and s2 % 2 != 0:
    print(s1 + s2 - a1)
elif s1 % 2 == 0 and s2 % 2 == 0:
    print(s1 + s2 - a2)
elif s1 % 2 != 0 and s2 % 2 != 0:
    print(s1 + s2 - a3)
    