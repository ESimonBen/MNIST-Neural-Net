import sys, math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Layer forward: given INPUT, WEIGHTS (M*N), BIAS (M), output sigmoid(W @ x + b)
data = sys.stdin.read().splitlines()
inp = wts = bias = []
M = N = 0
for line in data:
    if line.startswith("INPUT "):
        inp = list(map(float, line[6:].split(",")))
    elif line.startswith("WEIGHTS "):
        wts = list(map(float, line[8:].split(",")))
    elif line.startswith("BIAS "):
        bias = list(map(float, line[5:].split(",")))
    elif line.startswith("M "):
        parts = line.split()
        M = int(parts[1]); N = int(parts[3]) if len(parts) > 3 else len(inp)

if M and inp and wts and bias:
    out = []
    for i in range(M):
        z = sum(wts[i * N + j] * inp[j] for j in range(N)) + bias[i]
        out.append(f"{sigmoid(z):.4f}")
    print(",".join(out))
