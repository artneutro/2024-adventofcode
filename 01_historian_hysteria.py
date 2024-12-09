input = open('01_input.txt','r')
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


