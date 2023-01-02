def escape(line: str) -> str:
    return '"' + line.replace('\\', '\\\\').replace('"', '\\"') + '"'

def main(lines: list[str]) -> None:
    orig_len = 0
    rune_len = 0
    for line in lines:
        orig_len += len(line)
        rune_len += len(eval(line))
    print('Part1:', orig_len - rune_len)

    orig_len = 0
    escaped_len = 0
    for line in lines:
        orig_len += len(line)
        escaped_len += len(escape(line))
    print('Part2:', escaped_len - orig_len)

if __name__ == "__main__":
    import sys
    import time

    lines = open(sys.argv[1]).read().splitlines()
    start = time.perf_counter()
    main(lines)
    end = time.perf_counter()
    print(f"Time: {end - start:.2f}s")
