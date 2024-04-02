from math import *

def solve(x):
    return p * exp(-x) + q * sin(x) + r * cos(x) + s * tan(x) + t * x ** 2 + u

while True:
    try:
        values = list(map(int, input().split()))
    except EOFError:
        break
   
    p = values[0]
    q = values[1]
    r = values[2]
    s = values[3]
    t = values[4]
    u = values[5]

    if solve(0) < 0 or solve(1) > 0:
        print("No solution")
    else:
        left = 0
        right = 1

        for i in range(30):
            mid = (left + right) / 2
            if solve(mid) > 0:
                left = mid
            else:
                right = mid

        print(f"{left:.4f}")

    
    