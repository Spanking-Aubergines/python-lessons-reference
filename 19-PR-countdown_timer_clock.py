import time

secs = int(input("Set timer duration: (seconds)"))

for x in reversed(range(0,secs)):
    print(x+1)
    time.sleep(1)