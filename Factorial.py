# factorial recursive function
fact=1
def factrecur(n):
    if n==0:
     return 1
    else:
     return n*factrecur(n-1)
    
m=factrecur(5)
print("factorial is:",m)