def minimax(node, is_max):
    return node if isinstance(node, int) else (max if is_max else min)(minimax(c, not is_max) for c in node)

# Game tree structure: Root(MAX) -> MIN nodes -> MAX nodes -> Leaves
tree = [[[10, 9], [14, 18]], [[5, 4], [50, 3]]]

print(f"Root Optimal Value (MAX): {minimax(tree, False)}")