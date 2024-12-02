file = open('part2.txt', 'r');

locationID1 = []
locationID2 = []
for x in file:
    chars = x.split()
    locationID1.append(chars[0])
    locationID2.append(chars[1])

locationID1.sort()
locationID2.sort()

similarity = 0
for id1 in locationID1:
    count = 0
    for id2 in locationID2:
        if id2 == id1:
            count += 1
    similarity += int(id1) * count

print(similarity)
