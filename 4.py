from collections import deque

def solve_water_jug(cap_a, cap_b, target, mode='bfs'):
    frontier = [((0, 0), [(0, 0)])]
    visited = {(0, 0)}

    while frontier:
        # BFS uses pop(0) for queue (FIFO), DFS uses pop() for stack (LIFO)
        (a, b), path = frontier.pop(0) if mode == 'bfs' else frontier.pop()
        
        if a == target or b == target:
            return path

        # Pour amounts
        t1 = min(a, cap_b - b) # Pour A -> B
        t2 = min(b, cap_a - a) # Pour B -> A

        next_states = [
            (cap_a, b), (a, cap_b),  # Fill
            (0, b), (a, 0),          # Empty
            (a - t1, b + t1),        # Pour A to B
            (a + t2, b - t2)         # Pour B to A
        ]

        for state in next_states:
            if state not in visited:
                visited.add(state)
                frontier.append((state, path + [state]))
    return None

# Test with 3L and 5L jugs to measure 4L[cite: 7]
cap_a, cap_b, target = 3, 5, 4

for mode in ['bfs', 'dfs']:
    print(f"\n--- {mode.upper()} Solution Path ---")
    path = solve_water_jug(cap_a, cap_b, target, mode)
    for step, (a, b) in enumerate(path):
        print(f"Step {step}: Jug A = {a}L, Jug B = {b}L")