# Conditional Probability Tables (CPTs)
R = {True: 0.2, False: 0.8}
S = {True: {True: 0.01, False: 0.99}, False: {True: 0.4, False: 0.6}}
W = {(True, True): {True: 0.99, False: 0.01}, (True, False): {True: 0.9, False: 0.1}, 
     (False, True): {True: 0.9, False: 0.1}, (False, False): {True: 0.0, False: 1.0}}

# Exact inference via variable enumeration
def infer(w_obs):
    res = {r: sum(R[r] * S[r][s] * W[(r, s)][w_obs] for s in [True, False]) for r in [True, False]}
    total = sum(res.values())
    return {r: val / total for r, val in res.items()}

posterior = infer(True)
print(f"P(Rain = True | Wet = True): {posterior[True]:.4f}")
print(f"P(Rain = False | Wet = True): {posterior[False]:.4f}")