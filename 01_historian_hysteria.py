# https://adventofcode.com/2024/day/1

input = open('01_input.txt','r')

# Part 1
left = []
right = []
for line in input.readlines():
    items = line.split()
    left.append(items[0])
    right.append(items[1])
left = sorted(left)
right = sorted(right)
distance = 0
i = 0
while i < len(left) :
    distance = distance + abs(int(right[i]) - int(left[i]))
    i = i+1
print(distance)

# Part 2
repetitions = {}
for i in right:
    if i in repetitions:
        repetitions[i] = repetitions[i] + 1
    else:
        repetitions[i] = 1
similarity = 0
for i in left:
    if i in repetitions:
        similarity = similarity + (int(i)*repetitions[i])
print(similarity)





