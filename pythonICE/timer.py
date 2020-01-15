import time
n = time
def countdown(t):
    while t > 0:
        print (t)
        t = t -1
    if t ==0:
        print ("times up")
countdown(500000000)