nums = input().split()
nums = [int(i) for i in nums]
result = []

for element in nums:
    if element % 3 == 0:
        result.append(element)

print(*result)
