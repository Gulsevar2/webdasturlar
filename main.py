from random import *
from time import *
a=1
b=6
n=True
while n:
    print("Tosh tashlanyapti...")
    sleep(2)
    print("1-tosh",randint(a,b))
    print("2-tosh",randint(a,b))
    sleep(1)
    print("1.Ha")
    print("2.Yo'q")
    q=int(input("Yana tosh tashlansinmi?>>>  "))
    if q!=1:
        print("Dastur to'xtatildi!")
        n=False

