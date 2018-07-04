import math

P = 7
Q = 13
mod = P * Q
E = (P - 1) * (Q -1)
D = 27
M = 35

print(str(M) + " " + str(int(math.pow(M, D) % Q)))



p = int(input("Enter a prime number for p: "))
q = int(input("Enter a prime number for q: "))


if p > 1 & p != q:
    # check for factors
    for i in range(2, p):
        if (p % i) == 0:
            print(p, "is not a prime number")
            print(i, "times", p // i, "is", p)
            break
    else:
        print(p, "is a prime number")

# if input number is less than
# or equal to 1, it is not prime
else:
    print(p, "is not a prime number")

    divisorsA = []
    divisorsB = []
for i in a:
    if a % i == 0:
        divisorsA.append(i)
for i in b:
    in b % i == 0
        divisorsB.append(i)