n, carry = map(int, input().split())

cups = list(map(int, input().split()))

cups.sort()

if cups[0] * 2 <= cups[n]:
    p = cups[0]
else:
    p = cups[n] / 2.0

if p * 3 * n <= carry:
    print(p * 3 * n)
else:
    print(carry)
