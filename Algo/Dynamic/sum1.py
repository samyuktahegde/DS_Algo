#Number of ways to form a sum
#Eg (1,2,3) n=6
#state(n) = state(n-1)+state(n-2)+state(n-3)


def sumstates(n):
    if n<0:
        return 0
    if n==0:
        return 1
    return sumstates(n-1)+sumstates(n-2)+sumstates(n-3)

n = 6
print(sumstates(n))