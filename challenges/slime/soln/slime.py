n = int(input())

slime_list = []

for i in range(n):
    slime_list.append(1)

i = 1
while i < len(slime_list):
    if len(slime_list) == 1:
        break 
    elif slime_list[i] == slime_list[i - 1]:
        slime_list[i - 1] += 1
        slime_list.pop(i)
        i -= 1
    else:
        i += 1

print(*slime_list)
