#mahfuz



#writing the code for finding factorial
def fact(x):
    if x == 1:
        return 1
    return x * fact(x - 1)

print('The factorial should be: ', fact(3))


