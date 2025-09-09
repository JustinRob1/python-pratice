import math # you may use math.sqrt(x), but you do not have to.

n = int(input())

circle_list = []
point_list = []

for i in range(n):
	int_list = list(map(float, input().split()))
	circle_list.append(int_list)

m = int(input())

for i in range(m):
	x, y = map(float, input().split())
	for j in range(n):
		in_circle = False
		x_circle = circle_list[j][0]
		y_circle = circle_list[j][1]
		radius = circle_list[j][2]
		distance = math.sqrt((x_circle - x) ** 2 + (y_circle - y) ** 2)

		if distance <= radius:
			in_circle = True
			break

	if in_circle == True:
		print("Large")
	else:
		print("Small")
