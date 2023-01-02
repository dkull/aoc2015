import sys
import time
from functools import reduce

def wrapping(numbers: list[int]) -> int:
	# sort the numbers so smallest first
	main_sides = [
		(numbers[0] * numbers[1]),
		(numbers[1] * numbers[2]),
		(numbers[2] * numbers[0]),
	]
	slack = min(main_sides)
	return (sum(main_sides) * 2) + slack

def ribbon(numbers: list[int]) -> int:
	# product of numbers
	volume = reduce(lambda x, y: x * y, numbers)

	shortest = sys.maxsize
	side_pairs = [
		(numbers[0], numbers[1]),
		(numbers[1], numbers[2]),
		(numbers[2], numbers[0]),
	]
	for a, b in side_pairs:
		perimeter = (a + b) * 2
		if perimeter < shortest:
			shortest = perimeter

	return shortest + volume

def main(lines: list[str]) -> None:
	# extract all numbers from string
	numbers = [sorted(int(x) for x in line.split('x')) for line in lines]

	part1 = sum([wrapping(nums) for nums in numbers])
	print(f"Part 1: {part1}")
	part2 = sum([ribbon(nums) for nums in numbers])
	print(f"Part 2: {part2}")

if __name__ == '__main__':
	# read lines from args[1]
	lines = open(sys.argv[1]).readlines()
	lines = [l.strip() for l in lines]

	begin = time.time()
	main(lines)
	print(f'Time: {time.time() - begin} seconds')