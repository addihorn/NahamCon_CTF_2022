import random

flag = open('out', 'r').read()
ct = ''
#k = random.randrange(0,0xFFFD)
k = 39137
for c in flag:
    print((ord(c) - k) % 0xFFFD)
    ct += chr((ord(c) - k) % 0xFFFD)

open('flag.txt', 'w').write(ct)
