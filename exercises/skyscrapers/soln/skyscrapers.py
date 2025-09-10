from bisect import bisect
n = int(input())

skyscraper_list = []

for i in range(n):
    skyscraper_list.append(int(input()))

skyscraper_list.sort()

floor_num = 0
for i in range(max(skyscraper_list)):
	count = len(skyscraper_list) - bisect(skyscraper_list, floor_num)
	print(count)
	floor_num += 1
