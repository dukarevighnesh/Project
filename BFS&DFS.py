from collections import deque

G = {'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E', 'G'], 'G': ['F']}

def solve(start, goal, bfs=True):
    q, vis = [([start], start)], {start}
    while q:
        path, cur = (q.pop(0) if bfs else q.pop())
        if cur == goal: return path, len(path) - 1
        for n in (G[cur] if bfs else reversed(G[cur])):
            if n not in vis: vis.add(n); q.append((path + [n], n))

bfs_path, hops = solve('A', 'G', True)
dfs_path, _ = solve('A', 'G', False)

print(f"BFS Path: {bfs_path} | Minimum Hops: {hops}")
print(f"DFS Path: {dfs_path}")