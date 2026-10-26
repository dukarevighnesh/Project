import heapq

def a_star(graph, h, start, goal):
    pq = [(h[start], 0, start, [start])]
    visited = {}

    while pq:
        f, g, node, path = heapq.heappop(pq)
        if node == goal: return path, g
        if node in visited and visited[node] <= g: continue
        visited[node] = g

        for neighbor, weight in graph[node].items():
            ng = g + weight
            heapq.heappush(pq, (ng + h[neighbor], ng, neighbor, path + [neighbor]))

    return None, float('inf')

# Graph and Heuristics
graph = {
    'S': {'A': 3, 'D': 4},
    'A': {'S': 3, 'B': 4, 'D': 5},
    'B': {'A': 4, 'C': 4, 'E': 5},
    'C': {'B': 4},
    'D': {'S': 4, 'A': 5, 'E': 2},
    'E': {'B': 5, 'D': 2, 'F': 4},
    'F': {'E': 4, 'G': 3.5},
    'G': {'F': 3.5}
}

heuristics = {'S': 11.5, 'A': 10.1, 'B': 5.8, 'C': 3.4, 'D': 9.2, 'E': 7.1, 'F': 3.5, 'G': 0.0}

path, cost = a_star(graph, heuristics, 'S', 'G')
print(f"Optimal Path: {' -> '.join(path)}")
print(f"Total Cost: {cost}")