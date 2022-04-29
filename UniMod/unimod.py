import random

flag = open('flag.txt', 'r').read()
ct = ''
k = random.randrange(0,0xFFFD) # 65533
for c in flag:
    ct += chr((ord(c) + k) % 0xFFFD)

open('out', 'w').write(ct)
