import os
import random
import time
#live_file_tmp = open("live_log","r")
def read():
	file = open("accesslog","r")
	global live_file
	live_file = open("live_log","a")
	cnt = random_val()
	#Timer.start()
	#time.time()
	while (True):
		data = file.readline()
		if cnt == 0:
			time.sleep(2)
			cnt = random_val()
		else :
			write_log(str(data))
			cnt -=1

def write_log(data):
	#for line in data:
	live_file.write(data)
	#tmp=live_file_tmp.readline()


 	
def random_val():
	n = random.randrange(100,500,20)
	return n

if __name__ == '__main__':
	read() 

"""

#		THREADING

 
def read():
	file = open("log/access","r")
	
	while (True):
		data = file.readlines()
		write_log(n,data)
		#t = random.randrange(1,5,1)
		#time.sleep(6)


def write_log(n,data):
	for line in data:
		live_file.write(data)


if __name__ == '__main__':
	read()

"""

"""

   # ORIGINAL
   #LIVE DATA READ AND WRITE
live_file_tmp = open("live_log","r")
def read():
	file = open("log/access","r")
	global live_file
	live_file = open("live_log","a")
	while (True):
		#n = random.randrange(10,50,100)
		#print(n)
		data = file.readline()
		#pdb.set_trace()
		#print(data)
		#pdb.set_trace()
		write_log(str(data))
		#pdb.set_trace()
		#t = random.randrange(1,5,1)
		


def write_log(data):
	#for line in data:
	live_file.write(data)
	tmp=live_file_tmp.readline()
	print(tmp)
	#print(data)
	time.sleep(0.1)

if __name__ == '__main__':
	read()

	"""