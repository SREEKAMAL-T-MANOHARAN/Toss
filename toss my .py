import random
import time
toss = ('head','tail')

for i in range(101):
	time.sleep(0.5)
	win = random.choice(toss)
	print ('\n\033[1;32;40m',win)
        if win == "tales":
           print("\033[1;31;40m",win)
        else:
           print("\033[1;35;40m",win)


