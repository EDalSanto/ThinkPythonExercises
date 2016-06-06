def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

print gcd(100,44)
# 4

 # based on the observation that if r is the remainder when a is divided by b, then gcd(a, b) = gcd(b, r). As a base case, we can use gcd(a, 0) = a.
