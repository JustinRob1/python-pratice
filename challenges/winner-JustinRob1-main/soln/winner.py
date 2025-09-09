coins = int(input())
winner = ""

if coins % 3 == 0:
	winner = "Bob wins"
else:
	winner = "Alice wins"

print(winner)
