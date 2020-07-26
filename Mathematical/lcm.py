#Find the LCM of two numbers

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a, a)

def lcm(a,b):
    return (a*b)//gcd(a,b)   

print(lcm(15,20))

