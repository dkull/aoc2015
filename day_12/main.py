from typing import Any


def sum_object(obj: list[Any] | dict[Any, Any], ignore: bool) -> int:
    if isinstance(obj, list):
        return sum(sum_object(item, ignore) for item in obj)
    elif isinstance(obj, dict):
        if ignore and any(item == 'red' for item in obj.values()):
            return 0
        else:
            return sum(sum_object(item, ignore) for item in obj.values())
    elif isinstance(obj, int):
        return obj
    else:
        return 0

def main(data: list[Any] | dict[Any, Any]):
    print('Part1:', sum_object(data, False))
    print('Part2:', sum_object(data, True))

if __name__ == "__main__":
    import sys
    import time

    data = eval(open(sys.argv[1]).read())
    start = time.time()
    main(data)
    print(f'Time: {time.time() - start:.3f}')
