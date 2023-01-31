from collections import defaultdict

def is_possible(database: dict) -> bool:
    def dfs(node, color):
        colors[node] = color
        for neighbor in graph[node]:
            if colors[neighbor] == color:
                return False
            if colors[neighbor] == 0 and not dfs(neighbor, -color):
                return False
        return True

    graph = defaultdict(list)
    for node, neighbors in database.items():
        for neighbor in neighbors:
            graph[node].append(neighbor)
            graph[neighbor].append(node)

    colors = defaultdict(int)
    for node in graph:
        if colors[node] == 0:
            if not dfs(node, 1):
                return False
    return True