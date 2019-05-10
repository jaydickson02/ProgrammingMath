import random
x = 0

def isPrime(value):
    x = value
    y = value
    while True:
        y -= 1
        #print(y)
        if y == 1:
            return(x)
        if x % y == 0:
            print('false')
            return()

while True:
    value = random.randint(2, 10000)
    prime = isPrime(value)
    if prime:
        print(prime)
        #x += 1
        #print(x)
