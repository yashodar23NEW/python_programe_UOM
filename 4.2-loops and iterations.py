#01

val = int(input(''))
for x in range (0, val):
    for y in range(0,val):
      print('*',end='')
    print('')


#02

i = int(input())
j = 2
while j * j <= i:
    if not(i % j):
        print("not a prime")
        break
    j += 1  # Increment j by 1, not by 2
else:
    print("prime")




