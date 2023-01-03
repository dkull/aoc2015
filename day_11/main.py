

def increment_string(inp: str) -> str:
    """
    string 'abc' becomes 'abd'
    string 'xyz' becomes 'xza'
    only a-z
    """
    if not inp:
        return 'a'
    if inp[-1] == 'z':
        return increment_string(inp[:-1]) + 'a'
    return inp[:-1] + chr(ord(inp[-1]) + 1)

def is_suitable(inp: str) -> bool:
    # check for iol
    if any(x in inp for x in 'iol'):
        return False
    # check for pairs
    pairs = []
    skipto = 0
    for x in range(len(inp)-1):
        if x < skipto:
            continue
        if inp[x] == inp[x+1]:
            pairs.append(inp[x])
            skipto = x+2
    if len(pairs) < 2:
        return False
    # check for increasing 3
    buf: list[str] = []
    for y in inp:
        if not buf or ord(y) == ord(buf[-1])+1:
            buf.append(y)
            if len(buf) == 3:
                return True
        else:
            buf = [y]
    return False

def main(inp: str):
    while not is_suitable(inp):
        inp = increment_string(inp)
    print('Part1:', inp)

    inp = increment_string(inp)
    while not is_suitable(inp):
        inp = increment_string(inp)
    print('Part2:', inp)

if __name__ == '__main__':
    import sys
    import time

    inp = sys.argv[1]
    start = time.time()
    main(inp)
    print(f'Time: {time.time() - start:.3f}')

