import random
import time
toss = ('\033[1;34;40mhead','tail')

for i in range(101):
	time.sleep(0.5)
	win = random.choice(toss)
	print ('\n\033[1;32;40m',win)

