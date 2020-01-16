import time

how_long = int(input("How many minutes would you like time"))
settimmer = (how_long * 60)

def countdown(t):
    while t > 0:
        print (t)
        t = t -1
        time.sleep(1)
    if t ==0:
        print ("times up")
    
countdown( settimmer )