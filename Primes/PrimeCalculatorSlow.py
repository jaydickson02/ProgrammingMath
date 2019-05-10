import time



x = 3
y = x
high_prime = x
count = 0
start = time.clock()
while count != 2000:
    y -= 1
    if y == 1:
        high_prime = x
        count += 1
        x += 1
        y = x
    elif x % y == 0:
        x += 1
        y = x

print(time.clock() - start)
print(count)
print('High Prime: ' + str(high_prime))
#highest prime = 78283
