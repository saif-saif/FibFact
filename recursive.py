def myFib(x):
    if (x <= 1):
        return(1)
    else:
        return x + myFib(x-1)

def myFact(x):
    if (x <= 1):
        return(1)
    else:
        return x * myFact(x-1)

y = myFib(5)
z = myFact(5)
print(y,z)
