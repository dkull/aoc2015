import time
import hashlib

def main():
	inp = "ckczppom"

	newmd5 = hashlib.md5
	fivefound = False
	for x in range(2**32):
		md5 = newmd5()
		md5.update (f'{inp}{x}'.encode())
		
		zeros = 0
		for b in md5.digest():
			if b == 0x00:
				zeros += 2
			elif b >> 4 == 0:
				zeros += 1
				break
			else:
				break
		if zeros == 6:
			print('Part2:', x)
			break
		elif not fivefound and zeros == 5: 
			fivefound = True 
			print('part1:', x)

if __name__ == '__main__':
	begin = time.time()
	main()
	print(time.time() - begin)
