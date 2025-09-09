n, m = map(int, input().split())
k_list = []
total = 0
for i in range(n, 0, -1):
	total += i
	k_list.append(i)
	if total == m:
		break
	if total > m:
		total -= i
		k_list.pop(len(k_list) - 1)

k_list.reverse()
print(len(k_list))
print(*k_list)