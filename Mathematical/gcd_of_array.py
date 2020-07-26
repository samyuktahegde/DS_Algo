def gcd(x, y):
    if x==0:
        return y
    else:
        return gcd(y%x, x)

array = [2, 4, 6, 8, 16]
n = len(array)
g_c_d = gcd(array[0], array[1])
for i in range(2, n):
    g_c_d = gcd(g_c_d, array[i])
print(g_c_d)