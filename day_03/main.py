import time
import sys

def run(line: str) -> dict[tuple[int, int], int]:
	visited: dict[tuple[int, int], int] = {}
	at = (0, 0)
	visited[at] = 1
	# symbols are <>^v
	for symbol in line:
		match symbol:
			case "<":
				at = (at[0] - 1, at[1])
			case ">":
				at = (at[0] + 1, at[1])
			case "^":
				at = (at[0], at[1] - 1)
			case "v":
				at = (at[0], at[1] + 1)
		visited[at] = visited.get(at, 0) + 1
	return visited

def main(line: str) -> None:
	p1 = run(line)
	print("Part1:", len(p1))
	p2 = run(line[1::2]) | run(line[::2])
	print("Part2:", len(p2))

if __name__ == "__main__":
	# read file from args[1] with newlines stripped
	line = open(sys.argv[1], 'r').read().replace('\n', '')
	begin = time.time()
	main(line)
	print("Time elapsed: %s" % (time.time() - begin))