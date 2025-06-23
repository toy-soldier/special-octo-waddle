from typing import Self

import exceptions


class WeightedGraph:
    class _Node:
        def __init__(self, label: str):
            self.label = label
            self.edges = set()

        def __str__(self):
            return self.label

        def add_edge(self, dest: Self, weight: int) -> None:
            self.edges.add(WeightedGraph._Edge(self, dest, weight))

        def get_edges(self) -> set["WeightedGraph._Edge"]:
            return self.edges

    class _Edge:
        def __init__(self, src: "WeightedGraph._Node", dest: "WeightedGraph._Node", weight: int) -> None:
            self.src = src
            self.dest = dest
            self.weight = weight

        def __str__(self):
            return f"{self.src}->{self.dest}"

    class _NodeEntry:
        def __init__(self, node: "WeightedGraph._Node", priority: int):
            self.node = node
            self.priority = priority

    class _PriorityQueue:
        def __init__(self):
            self.queue = []

        def enqueue(self, node_entry: "WeightedGraph._NodeEntry") -> None:
            self.queue.append(node_entry)
            self.queue.sort(key=lambda item: item.priority)

        def dequeue(self) -> "WeightedGraph._NodeEntry":
            return self.queue.pop(0)

        def is_empty(self) -> bool:
            return len(self.queue) == 0

    def __init__(self):
        self._vertices = {}

    def __str__(self):
        edges = []
        for node in self._vertices.values():
            for edge in node.get_edges():
                edges.append(str(edge))
        return  ", ".join(edges)

    def add_node(self, label: str) -> None:
        if label not in self._vertices:
            self._vertices[label] = self._Node(label)

    def add_edge(self, src: str, dest: str, weight: int) -> None:
        src_node = self._vertices.get(src)
        dest_node = self._vertices.get(dest)
        if not src_node or not dest_node:
            raise exceptions.IllegalArgumentException("Node/s not found")
        src_node.add_edge(dest_node, weight)
        dest_node.add_edge(src_node, weight)

    def _init_for_shortest_path(self, src: str, dest: str) -> (
            tuple)[_PriorityQueue, set[_Node], dict[_Node, tuple[int, _Node | None]]]:
        src_node = self._vertices.get(src)
        dest_node = self._vertices.get(dest)
        if not src_node or not dest_node:
            raise exceptions.IllegalArgumentException("Node/s not found")
        queue = self._PriorityQueue()
        nodes_table = {vertex: (1_000_000, None) for vertex in self._vertices.values()}
        nodes_table[src_node] = (0, None)

        queue.enqueue(self._NodeEntry(src_node, priority=0))
        return queue, set(), nodes_table

    def shortest_path(self, src: str, dest: str) -> str:
        queue, visited, nodes_table = self._init_for_shortest_path(src, dest)
        while not queue.is_empty():
            entry = queue.dequeue()
            node = entry.node
            for edge in node.get_edges():
                dest_node = edge.dest
                if dest_node in visited:
                    continue
                weight = entry.priority + edge.weight
                if weight < nodes_table[dest_node][0]:
                    nodes_table[dest_node] = (weight, node)
                queue.enqueue(self._NodeEntry(dest_node, priority=weight))
            visited.add(node)
        return self._get_path(src, dest, nodes_table)

    def _get_path(self, src: str, dest: str,
                  nodes_table: dict[_Node, tuple[int, _Node | None]]) -> str:
        path = []
        dest_node = self._vertices[dest]
        weight = nodes_table[dest_node][0]
        while dest_node:
            path.append(dest_node.label)
            dest_node = nodes_table[dest_node][1]
        return f"Shortest path from {src} to {dest} is {'->'.join(path[::-1])} ({weight=})"

    def has_cycle(self) -> bool:
        visited = set()
        node_table = {}
        for vertex in self._vertices.values():
            if vertex in visited:
                continue
            node_table[vertex.label] = None
            result = self._has_cycle(vertex, None, visited, node_table)
            if result:
                path = []
                dest = node_table["cycle@"]
                while dest:
                    path.append(dest)
                    dest = node_table[dest]
                print(f"Cycle detected at {'->'.join(path[::-1])}")
                return result
        return False

    def _has_cycle(self, current: _Node, parent: _Node | None, visited: set[_Node],
                   node_table: dict[str, str | None]) -> bool:
        visited.add(current)
        for edge in current.get_edges():
            neighbor = edge.dest
            if neighbor == parent:
                continue
            if neighbor in visited:
                node_table["cycle@"] = current.label
                return True
            node_table[neighbor.label] = current.label
            if self._has_cycle(neighbor, current, visited, node_table):
                return True
        return False



def main() -> None:
    g = WeightedGraph()
    for label in "A", "B", "C", "D", "E":
        g.add_node(label)
    g.add_edge("A", "B", 3)
    g.add_edge("A", "D", 2)
    g.add_edge("A", "C", 4)
    g.add_edge("D", "B", 6)
    g.add_edge("D", "C", 1)
    g.add_edge("E", "B", 1)
    g.add_edge("E", "D", 5)
    a = g.shortest_path("A", "E")
    g = WeightedGraph()
    for label in "A", "B", "C":
        g.add_node(label)
    g.add_edge("A", "B", 3)
    g.add_edge("B", "C", 2)
    g.add_edge("C", "A", 2)
    a = g.has_cycle()
    print()


if __name__ == '__main__':
    main()
