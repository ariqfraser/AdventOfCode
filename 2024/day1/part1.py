file = open('part1.txt', 'r') 

locationID1 = []
locationID2 = []
for x in file:
    chars = x.split()
    locationID1.append(chars[0])
    locationID2.append(chars[1])

locationID1.sort()
locationID2.sort()

distances = []

for i, id1 in enumerate(locationID1):
    id2 = locationID2[i]
    distances.append(abs(int(id1)-int(id2))) 

sum_dist = sum(distances)
print(sum_dist)
