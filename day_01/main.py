import time
import sys

def main(line: str) -> None:
	opens = line.count('(')
	closes = line.count(')')
	print("Part1:", opens - closes)

	pos = 0
	for i, char in enumerate(line):
		match char:
			case '(': pos += 1
			case ')': pos -= 1
		if pos == -1:
			print("Part2:", i + 1)
			break



if __name__ == '__main__':
	lines = open(sys.argv[1], 'r').read().split('\n')
	begin = time.time()
	main(lines[0])
	print("Time:", time.time() - begin)