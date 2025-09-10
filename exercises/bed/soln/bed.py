# read in the input
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

# solve the problem
width = x2 - x1
height = y2 - y1

if x1 > x2:
	width = x1 - x2

if y1 > y2:
	height = y1 - y2

area = height * width

# output the result
print(area)