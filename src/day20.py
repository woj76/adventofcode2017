#!/snap/bin/pypy3

from aoc import repres

part2 = True

positions = []
velocities = []
accelerations = []

with open("../data/day20.txt", "rt") as file:
	for x in file.read().strip().split('\n'):
		[p, v, a] = x.split(', ')
		positions.append(tuple([int(x) for x in p[3:-1].split(',')]))
		velocities.append(tuple([int(x) for x in v[3:-1].split(',')]))
		accelerations.append(tuple([int(x) for x in a[3:-1].split(',')]))

total = len(positions)

distances = [0] * total

for _ in range(50 if part2 else 500):
	for i in range(total):
		if positions[i] == None:
			continue
		px,py,pz = positions[i]
		vx,vy,vz = velocities[i]
		ax,ay,az = accelerations[i]
		vx, vy, vz = vx + ax, vy + ay, vz + az
		px, py, pz = px + vx, py + vy, pz + vz
		positions[i] = (px,py,pz)
		velocities[i] = (vx,vy,vz)
		if not part2:
			distances[i] = abs(px) + abs(py) + abs(pz)
	if part2:
		indexes = [i for i in range(total) if positions.count(positions[i]) > 1]
		for i in indexes:
			positions[i] = None
	else:
		min_pos = distances.index(min(distances))

r = total - positions.count(None) if part2 else min_pos

repres(r, part2)
