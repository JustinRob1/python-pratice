days = int(input())
n = list(map(int, input().split()))

min_price = max(n)
current = 0
max_profit = 0

for i in range(0, len(n)):
	current = n[i] - min_price
	if n[i] < min_price:
		min_price = n[i]
	if current > max_profit:
		max_profit = current

print(max_profit)
