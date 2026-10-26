import numpy as np

states, obs = ['Sunny', 'Rainy'], {'Dry': 0, 'Humid': 1, 'Wet': 2}
pi, A, B = np.array([0.6, 0.4]), np.array([[0.8, 0.2], [0.4, 0.6]]), np.array([[0.6, 0.3, 0.1], [0.1, 0.4, 0.5]])

def viterbi(seq):
    T, N = len(seq), len(states)
    dp, bp = np.zeros((N, T)), np.zeros((N, T), dtype=int)
    dp[:, 0] = pi * B[:, obs[seq[0]]]
    
    for t in range(1, T):
        o = obs[seq[t]]
        for j in range(N):
            p = dp[:, t-1] * A[:, j] * B[j, o]
            dp[j, t], bp[j, t] = np.max(p), np.argmax(p)
            
    path = [np.argmax(dp[:, -1])]
    for t in range(T - 1, 0, -1): path.insert(0, bp[path[0], t])
    return [states[i] for i in path], np.max(dp[:, -1])

seq = ['Dry', 'Humid', 'Wet', 'Wet', 'Humid']
path, prob = viterbi(seq)
print(f"Estimated Weather States: {path}")
print(f"Sequence Probability: {prob:.6f}")