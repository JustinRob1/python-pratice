import math
# take in input
numbers = list(map(int, input().split()))

# solve the problem
total = 0
for i in range(0, len(numbers)):
	total += numbers[i]	

average = total / len(numbers)
# output the solution
print(math.floor(average))
