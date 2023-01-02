import sys
import time

from typing import Callable


class BaseOp:
    @classmethod
    def parse(cls, value: str) -> 'BaseOp | None':
        pass

    def get_value(self, ops: list['BaseOp']) -> int:
        pass

    def resolve(self, thing: str | int, ops: list['BaseOp']) -> int:
        if isinstance(thing, int) or thing.isdigit():
            return int(thing)
        return ops[thing].get_value(ops)

class Variable(BaseOp):
    def __init__(self, name: str):
        self.name = name

    @classmethod
    def parse(cls, value: str) -> 'BaseOp | None':
        if value.isalpha():
            return cls(value)

    def get_value(self, ops: list['BaseOp']) -> int:
        return ops[self.name].get_value(ops)

class Literal(BaseOp):
    def __init__(self, value):
        self.value = value

    @classmethod
    def parse(cls, value: str) -> 'BaseOp | None':
        if value.isdigit():
            return Literal(int(value))
        return None

    def get_value(self, ops: list['BaseOp']) -> int:
        return self.value

class And(BaseOp):
    def __init__(self, left: int | str, right: int | str):
        self.left = left
        self.right = right

    @classmethod
    def parse(cls, value: str) -> 'And | None':
        if ' AND ' not in value:
            return None
        a, b = value.split(' AND ')
        return And(a, b)

    def get_value(self, ops: list[BaseOp]) -> int:
        return self.resolve(self.left, ops) & self.resolve(self.right, ops)

class Or(BaseOp):
    def __init__(self, left: int | str, right: int | str):
        self.left = left
        self.right = right

    @classmethod
    def parse(cls, value: str) -> 'Or | None':
        if ' OR ' not in value:
            return None
        a, b = value.split(' OR ')
        return Or(a, b)

    def get_value(self, ops: list[BaseOp]) -> int:
        self.left = self.resolve(self.left, ops)
        self.right = self.resolve(self.right, ops)
        return self.left | self.right

class RShift(BaseOp):
    def __init__(self, left: int | str, right: int | str):
        self.left = left
        self.right = right

    @classmethod
    def parse(cls, value: str) -> 'RShift | None':
        if ' RSHIFT ' not in value:
            return None
        a, b = value.split(' RSHIFT ')
        return RShift(a, b)

    def get_value(self, ops: list[BaseOp]) -> int:
        return self.resolve(self.left, ops) >> self.resolve(self.right, ops)

class LShift(BaseOp):
    def __init__(self, left: int | str, right: int | str):
        self.left = left
        self.right = right

    @classmethod
    def parse(cls, value: str) -> 'LShift | None':
        if ' LSHIFT ' not in value:
            return None
        a, b = value.split(' LSHIFT ')
        return LShift(a, b)

    def get_value(self, ops: list[BaseOp]) -> int:
        return self.resolve(self.left, ops) << self.resolve(self.right, ops)

class Not(BaseOp):
    def __init__(self, value: int | str):
        self.value = value

    @classmethod
    def parse(cls, value: str) -> 'Not | None':
        if value.startswith('NOT '):
            return Not(value[4:])
        return None

    def get_value(self, ops: list[BaseOp]) -> int:
        return ~self.resolve(self.value, ops) & 0xFFFF

ops: list[Callable[[str], [BaseOp]]] = [
    Variable.parse,
    Literal.parse,
    And.parse,
    Or.parse,
    RShift.parse,
    LShift.parse,
    Not.parse,
]

def main(lines: list[str]) -> None:
    data: dict[str, BaseOp] = {}
    for line in lines:
        for op in ops:
            left, right = line.split(' -> ')
            op = op(left)
            if op is not None:
                data[right] = op
                break
        else:
            print("failed to parse line:", line)

    a = data['a'].get_value(data)
    print('Part1:', a)

    data: dict[str, BaseOp] = {}
    for line in lines:
        for op in ops:
            left, right = line.split(' -> ')
            if right == 'b':
                left = str(a)
            op = op(left)
            if op is not None:
                data[right] = op
                break
        else:
            print("failed to parse line:", line)
    a = data['a'].get_value(data)
    print('Part2:', a)

if __name__ == '__main__':
    # read file lines from args[1]
    lines = open(sys.argv[1]).read().splitlines()
    begin = time.time()
    main(lines)
    print(f'Finished in {time.time() - begin} seconds')
