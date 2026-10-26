import heapq

G = ((1, 2, 3), (8, 0, 4), (7, 6, 5))
h = lambda b: sum(b[i][j] and b[i][j] != G[i][j] for i in range(3) for j in range(3))

def solve(b):
    q, vis = [(h(b), 0, b, [b])], set()
    while q:
        _, g, cur, path = heapq.heappop(q)
        if cur == G: return path
        if cur in vis: continue
        vis.add(cur)
        r, c = next((i, j) for i in range(3) for j in range(3) if not cur[i][j])
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= (nr := r + dr) < 3 and 0 <= (nc := c + dc) < 3:
                lst = [list(row) for row in cur]
                lst[r][c], lst[nr][nc] = lst[nr][nc], lst[r][c]
                nt = tuple(tuple(row) for row in lst)
                if nt not in vis: heapq.heappush(q, (g + 1 + h(nt), g + 1, nt, path + [nt]))

for i, step in enumerate(solve(((2, 8, 3), (1, 6, 4), (7, 0, 5)))):
    print(f"Step {i}: {step}")