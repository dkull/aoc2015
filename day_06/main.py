import enum

class RuleType(enum.Enum):
	ON = 1
	OFF = 2
	TOGGLE = 3

class Rule:
	def __init__(self, line: str) -> None:
		self.rule_type = self.get_rule_type(line)
		self.from_x, self.from_y, self.to_x, self.to_y = self.parse_coords(line)

	def get_rule_type(self, line: str) -> RuleType:
		if line.startswith('turn on'):
			return RuleType.ON
		elif line.startswith('turn off'):
			return RuleType.OFF
		elif line.startswith('toggle'):
			return RuleType.TOGGLE
		else:
			raise ValueError(f'Unknown rule type: {line}')

	def parse_coords(self, line: str) -> tuple[int, int, int, int]:
		"""
		parse rules like:
		> turn on 212,957 through 490,987
		> toggle 171,31 through 688,88
		> turn off 991,989 through 994,998
		i need the number pairs
		"""
		split = line.split(' ')
		splitter_idx = split.index('through')
		first = split[splitter_idx - 1]
		second = split[splitter_idx + 1]
		return tuple(map(int, first.split(','))) + tuple(map(int, second.split(',')))

class RuleMachine:
	def __init__(self, lines: list[str]):
		self.rules = [Rule(line) for line in lines]

	def get_p1_state(self, x: int, y: int) -> RuleType:
		state = RuleType.OFF
		for rule in self.rules:
			# if rule applies
			if rule.from_x <= x <= rule.to_x and rule.from_y <= y <= rule.to_y:
				match (state, rule.rule_type):
					case (RuleType.ON, RuleType.OFF):
						state = RuleType.OFF
					case (RuleType.ON, RuleType.TOGGLE):
						state = RuleType.OFF
					case (RuleType.OFF, RuleType.ON):
						state = RuleType.ON
					case (RuleType.OFF, RuleType.TOGGLE):
						state = RuleType.ON

		return state

	def get_p2_state(self, x: int, y: int) -> int:
		brightness = 0
		for rule in self.rules:
			# if rule applies
			if rule.from_x <= x <= rule.to_x and rule.from_y <= y <= rule.to_y:
				match rule.rule_type:
					case RuleType.ON:
						brightness += 1
					case RuleType.OFF:
						brightness -= 1 if brightness > 0 else 0
					case RuleType.TOGGLE:
						brightness += 2

		return brightness

# lines is from file in args[1]
def main(lines: list[str]) -> None:
	rm = RuleMachine(lines)

	p1 = 0
	p2 = 0
	for y in range(1000):
		print(y)
		for x in range(1000):
			if rm.get_p1_state(x, y) == RuleType.ON:
				p1 += 1
			p2 += rm.get_p2_state(x, y)
	print("Part1:", p1)
	print("Part2:", p2)

if __name__ == '__main__':
	import sys, time
	with open(sys.argv[1]) as f:
		lines = f.readlines()
	begin = time.time()
	main(lines)
	print(time.time() - begin)