n, carry = map(int, input().split())

cups = list(map(int, input().split()))

boys = cups[0]
girls = cups[n]
res = 0
waterBoy = 0
waterGirl = 0
water = 0.5 

while res <= carry and waterGirl <= girls and waterBoy <= boys:
    prev = res
   
    waterGirl = water * n
    waterBoy = water * 2 * n
    res = waterBoy + waterGirl
    water += 0.5

print(int(prev))
    