import sys
import math
for line in sys.stdin:
    line = line.rstrip("\n").strip()
    if not line: continue
    x = float(line)
    print(f"{1 / (1 + math.exp(-x)):.4f}")
