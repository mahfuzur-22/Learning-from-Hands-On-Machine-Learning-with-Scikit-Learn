def factorial1 (n):
    fact1=1
    for i in range (1, n+1, 1):
        fact1 *=i
    return fact1
result= factorial1 (5)

print("factorial is:", result)


def factorial2(n):
    if n==0:
     return 1
    else:
     return n*factorial2(n-1)

result2=factorial2(4)
print("now factoria is:", result2) 

    