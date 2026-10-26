from collections import deque

# Initial and Goal states[cite: 41, 42]
init = frozenset({"On(A,B)", "On(B,Table)", "Clear(A)", "Clear(Table)"})
goal = frozenset({"On(B,A)", "On(A,Table)"})

# Valid actions: (Name, Preconditions, Add List, Delete List)
actions = [
    ("Move(A,B,Table)", {"On(A,B)", "Clear(A)"}, {"On(A,Table)", "Clear(B)"}, {"On(A,B)"}),
    ("Move(B,Table,A)", {"On(B,Table)", "Clear(B)", "Clear(A)"}, {"On(B,A)"}, {"On(B,Table)", "Clear(A)"})
]

q, vis = deque([(init, [])]), {init}
while q:
    state, plan = q.popleft()
    if goal.issubset(state):
        for i, step in enumerate(plan, 1): print(f"Step {i}: {step}")
        break
    for name, pre, add, delete in actions:
        if pre.issubset(state) and (nxt := (state - delete) | add) not in vis:
            vis.add(nxt)
            q.append((nxt, plan + [name]))