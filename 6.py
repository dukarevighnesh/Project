import random, math

dist = lambda r, m: sum(m[r[i]][r[(i+1)%len(r)]] for i in range(len(r)))

def solve(m):
    n, pop = len(m), [random.sample(range(len(m)), len(m)) for _ in range(20)]
    
    # 1. GA Global Search
    for _ in range(30): 
        pop.sort(key=lambda r: dist(r, m))
        pop = pop[:2] + [random.sample(range(n), n) for _ in range(18)]
    
    best = min(pop, key=lambda r: dist(r, m))
    curr, cost, best_c, temp = list(best), dist(best, m), dist(best, m), 500
    
    # 2. SA Local Refinement
    for _ in range(200):
        i, j = sorted(random.sample(range(n), 2))
        new_r = curr[:i] + curr[i:j+1][::-1] + curr[j+1:]
        new_c = dist(new_r, m)
        if new_c < cost or random.random() < math.exp((cost - new_c) / temp):
            curr, cost = new_r, new_c
            if cost < best_c: best, best_c = list(curr), cost
        temp *= 0.99
        
    return best, best_c

matrix = [[0, 29, 20, 21], [29, 0, 15, 17], [20, 15, 0, 28], [21, 17, 28, 0]]
route, cost = solve(matrix)
print(f"Route: {route}\nCost: {cost}")