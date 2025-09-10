# Read in the input
a, b = map(int, input().split())
# Solve the problem
total = a - b
if total < 0:
	total *= -1
# Output the result
print(total)