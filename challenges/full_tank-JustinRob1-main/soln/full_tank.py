# Good luck on this morning problem!
l, c, n, t = map(int, input().split())
stops = list(map(int, input().split()))

stops.insert(0, 0)
stops.append(l)
time = l
tank = c
i = 0

while i < n + 1:
    tank -= (stops[i+1] - stops[i])
    if tank < 0:
        tank = c
        time += t
    else:
    	i += 1

print(time)
