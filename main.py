import sys, math
for raw in sys.stdin:
    line = raw.rstrip("\n").strip()
    if not line: continue
    x_str, w_str, b_str = line.split(";")
    x = list(map(float, x_str.split(",")))
    w = list(map(float, w_str.split(",")))
    b = float(b_str)

    z = sum(wi * xi for wi, xi in zip(w, x)) + b
    sigmoid = 1.0 / (1.0 + math.exp(-z))
    print(round(sigmoid, 4))