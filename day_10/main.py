
def split_on_change(inp: str) -> list[str]:
    parts = []
    part = ""
    for n in inp:
        if part == "" or n == part[-1]:
            part += n
        else:
            parts.append(part)
            part = n
    parts.append(part)
    return parts

def new_seq(inp: list[str]) -> str:
    return "".join([str(len(part)) + part[0] for part in inp])

def main(_inp: int):
    inp = str(_inp)
    for i in range(50):
        inp = new_seq(split_on_change(inp))
        if i == 39:
            print('Part1:', len(inp))
        if i == 49:
            print('Part2:', len(inp))

if __name__ == "__main__":
    import sys
    import time

    line = int(open(sys.argv[1]).readline())
    start = time.time()
    main(line)
    print(time.time() - start)

