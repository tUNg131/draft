import random

def rand(n):
    counter = 0
    for i in range(n):
        if random.randint(1,6) == 1:
            counter += 1
    return counter

arr = []

def dice(n):
    if n == 0:
        return
    else:
        x = rand(n)
        arr.append(x)
        dice(x)

dice(10000000)

print(arr)
