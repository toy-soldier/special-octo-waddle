import exceptions


class Graph:

    class _Node:

        def __init__(self, label: str):
            self.label = label

        def __str__(self):
            return f"{self.label}"

    def __init__(self):
        self._vertices = {}
        self._edges = {}

    def __str__(self):
        return ", ".join([f"{k} -> {[str(node) for node in v]}" for k, v in self._edges.items()])

    def add_node(self, label: str) -> None:
        if label not in self._vertices:
            node = self._Node(label)
            self._vertices[label] = node
            self._edges[node] = set()

    def remove_node(self, label: str) -> None:
        if label not in self._vertices:
            return
        node = self._vertices.pop(label)
        self._edges.pop(node)
        for connections in self._edges.values():
            connections.discard(node)

    def add_edge(self, src: str, dest: str):
        src_node = self._vertices.get(src)
        dest_node = self._vertices.get(dest)
        if not src_node or not dest_node:
            raise exceptions.IllegalArgumentException("Node/s not found.")
        self._edges[src_node].add(dest_node)

    def remove_edge(self, src: str, dest: str):
        src_node = self._vertices.get(src)
        dest_node = self._vertices.get(dest)
        if not src_node or not dest_node:
            return
        self._edges[src_node].remove(dest_node)

    def depth_first_traversal(self, label: str) -> list[str]:
        traversal = []
        node = self._vertices.get(label)
        if node:
            self._depth_first_traversal(node, set(), traversal)
        return traversal

    def _depth_first_traversal(self, node: _Node, visited_nodes: set[_Node],
                               traversal: list[str]) -> None:
        traversal.append(node.label)
        visited_nodes.add(node)
        for neighbor in self._edges[node]:
            if neighbor not in visited_nodes:
                self._depth_first_traversal(neighbor, visited_nodes, traversal)

    def iterative_depth_first_traversal(self, label: str) -> list[str]:
        node = self._vertices.get(label)
        if not node:
            return []

        traversal = []
        visited_nodes = set()
        pending = [node]
        while len(pending) > 0:
            current = pending.pop()
            if current in visited_nodes:
                continue
            traversal.append(current.label)
            visited_nodes.add(current)
            for neighbor in self._edges[current]:
                pending.append(neighbor)
        return traversal

    def breadth_first_traversal(self, label: str) -> list[str]:
        node = self._vertices.get(label)
        if not node:
            return []

        traversal = []
        visited_nodes = set()
        pending = [node]
        while len(pending) > 0:
            current = pending.pop(0)
            if current in visited_nodes:
                continue
            traversal.append(current.label)
            visited_nodes.add(current)
            for neighbor in self._edges[current]:
                pending.append(neighbor)
        return traversal

    def topological_sort(self) -> list[str]:
        stack = []
        visited_nodes = set()
        for vertex in self._vertices.values():
            self._topological_sort(vertex, visited_nodes, stack)
        stack.reverse()
        return stack

    def _topological_sort(self, node: _Node, visited_nodes: set[_Node],
                               stack: list[str]) -> None:
        if node in visited_nodes:
            return
        visited_nodes.add(node)
        for neighbor in self._edges[node]:
            self._topological_sort(neighbor, visited_nodes, stack)
        stack.append(node.label)

    def has_cycle(self) -> bool:
        visiting = set()
        visited = set()
        path = {}
        cycle = []
        for vertex in self._vertices.values():
            path = {vertex.label: None}
            if self._has_cycle(vertex, visiting, visited, path):
                dest = path["cycle@"]
                while dest:
                    cycle.append(dest)
                    dest = path[dest]
                print(f"Cycle detected at {'->'.join(cycle[::-1])}")
                return True
        return False

    def _has_cycle(self, node: _Node, visiting: set[_Node], visited: set[_Node],
                   path: dict[str, str | None]) -> bool:
        visiting.add(node)
        for neighbor in self._edges[node]:
            if neighbor in visited:
                continue
            if neighbor in visiting:
                path["cycle@"] = node.label
                return True
            path[neighbor.label] = node.label
            if self._has_cycle(neighbor, visiting, visited, path):
                return True
        visiting.remove(node)
        visited.add(node)
        return False


def main() -> None:
    g = Graph()
    g.add_node("A")
    g.add_node("B")
    g.add_node("C")
    g.add_edge("A", "B")
    g.add_edge("B", "A")
    g.add_edge("C", "A")
    g.add_edge("C", "B")
    g.add_node("D")
    a = g.depth_first_traversal("A")
    b = g.iterative_depth_first_traversal("Z")
    c = g.breadth_first_traversal("D")

    g = Graph()
    for label in "X", "A", "B", "P":
        g.add_node(label)
    g.add_edge("X", "A")
    g.add_edge("X", "B")
    g.add_edge("A", "P")
    g.add_edge("B", "P")
    b = g.topological_sort()

    g = Graph()
    for label in "D", "A", "B", "C":
        g.add_node(label)
    g.add_edge("D", "A")
    g.add_edge("A", "B")
    g.add_edge("B", "C")
    g.add_edge("A", "C")
    print(f"{g.has_cycle()=}")


if __name__ == '__main__':
    main()
