word_list = list(map(int, input().split()))
current = 0
plat = 1

for i in range(0, len(word_list)):
	if word_list[i] == word_list[i - 1]:
		 current += 1
	else:
		current = 1

	if current >= plat:
		plat = current

print(plat)
