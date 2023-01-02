
import collections

def part1(lines: list[str]) -> None:
	nice_count = 0
	surely_naughty = set(['ab', 'cd', 'pq', 'xy'])

	for line in lines:
		digrams = set([''.join(x) for x in zip(line, line[1:])])
		if surely_naughty.intersection(digrams):
			continue

		# count letter appearance
		double_letter = any(n[0] == n[1] for n in digrams)
		if not double_letter:
			continue

		# count vowels
		counts = collections.Counter(line)
		vowels = 'aeiou'
		vowel_count = sum(counts[v] for v in vowels)
		if vowel_count < 3:
			continue

		nice_count += 1

	print("Part1:", nice_count)


def part2(lines: list[str]) -> None:
	nice_count = 0
	for line in lines:
		digrams = [''.join(x) for x in zip(line, line[1:])]

		digram_good = False
		for digram in digrams:
			# find count of non-overlapping instances of digram in line
			count = line.count(digram)
			if count >= 2:
				digram_good = True
		if not digram_good:
			continue

		trigrams = set([''.join(x) for x in zip(line, line[1:], line[2:])])
		if not any(v[0] == v[2] for v in trigrams):
			continue

		nice_count += 1

	print("Part2:", nice_count)

# 67 72
# lines is stripped lines from file in args[1]
def main(lines: list[str]) -> None:
	part1(lines)
	part2(lines)

if __name__ == "__main__":
	import sys, time
	with open(sys.argv[1], "r") as f:
		lines = f.read().splitlines()
	begin = time.time()
	main(lines)
	print(time.time() - begin)
