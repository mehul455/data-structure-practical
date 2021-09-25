from collections import defaultdict

def build_graph():
    edges = [
    ["A", "B"], ["A", "E"],
    ["A", "C"], ["B", "D"],
    ["B", "E"], ["C", "F"],
    ["C", "G"], ["D", "E"]
    ]
    graph = defaultdict(list)
    for edge in edges:
        a, b = edge[0], edge[1]
        graph[a].append(b)
        graph[b].append(a)
    return graph
if __name__ == "__main__":
    graph = build_graph()
    print(graph)