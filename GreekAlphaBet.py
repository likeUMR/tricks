from random import random


import random

while True:
    index=round(945+25*random.random())
    upDownIndex=round(random.random())
    if upDownIndex==0:
        print(chr(index).lower(),end='')
    else:
        print(chr(index).upper(),end='')
    input()
    