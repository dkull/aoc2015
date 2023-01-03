
class Node:
    def __init__(self, name: str):
        self.name: str = name

class Edge:
    def __init__(self, source: Node, target: Node, weight: int):
        self.source: Node = source
        self.target: Node = target
        self.weight: int = weight

def parse(lines: list[str]) -> tuple[dict[str, Node], dict[str, dict[str, int]]]:
    nodes: dict[str, Node] = {}
    edges: dict[str, dict[str, int]] = {}
    for line in lines:
        line = line.replace(' to ', ' ').replace(' = ', ' ')

        _source, _target, _weight = line.split(' ')
        weight = int(_weight)
        source = nodes.get(_source, Node(name=_source))
        target = nodes.get(_target, Node(name=_target))
        nodes[source.name] = source
        nodes[target.name] = target

        edge1 = Edge(source=source, target=target, weight=weight)
        if edge1.source.name not in edges:
            edges[edge1.source.name] = {}
        edges[edge1.source.name][edge1.target.name] = edge1.weight

        edge2 = Edge(source=target, target=source, weight=weight)
        if edge2.source.name not in edges:
            edges[edge2.source.name] = {}
        edges[edge2.source.name][edge2.target.name] = edge2.weight

    return nodes, edges

def find_shortest_path(nodes: dict[str, Node], edges: dict[str, dict[str, int]], visited: list[str],
                       distance: int) -> int:
    shortest = sys.maxsize
    if len(visited) == len(nodes):
        return distance

    if not visited:
        for node in nodes.values():
            result = find_shortest_path(nodes, edges, visited + [node.name], distance)
            shortest = min(shortest, result)
    else:
        currently_at = visited[-1]
        can_travel = edges.get(currently_at, {})
        for to_node, to_distance in can_travel.items():
            if to_node in visited:
                continue
            result = find_shortest_path(nodes, edges, visited + [to_node], distance + to_distance)
            shortest = min(shortest, result)

    return shortest

def find_longest_path(nodes: dict[str, Node], edges: dict[str, dict[str, int]], visited: list[str],
                       distance: int) -> int:
    longest = 0
    if len(visited) == len(nodes):
        return distance

    if not visited:
        for node in nodes.values():
            result = find_longest_path(nodes, edges, visited + [node.name], distance)
            longest = max(longest, result)
    else:
        currently_at = visited[-1]
        can_travel = edges.get(currently_at, {})
        for to_node, to_distance in can_travel.items():
            if to_node in visited:
                continue
            result = find_longest_path(nodes, edges, visited + [to_node], distance + to_distance)
            longest = max(longest, result)

    return longest

def main(lines: list[str]):
    nodes, edges = parse(lines)

    shortest = find_shortest_path(nodes, edges, [], 0)
    print('Part1:', shortest)

    longest = find_longest_path(nodes, edges, [], 0)
    print('Part2:', longest)

if __name__ == "__main__":
    import sys
    import time

    lines = open(sys.argv[1]).read().splitlines()
    start = time.time()
    main(lines)
    end = time.time()
    print(f"Time: {end - start}")
