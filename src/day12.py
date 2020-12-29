#!/snap/bin/pypy3

from aoc import repres

with open("../data/day12.txt", "rt") as file:
	data = [x.split(" <-> ") for x in file.read().strip().split('\n')]

part2 = True
r = 0

mapping = {}

for d in data:
	tos = [int(x.strip()) for x in d[1].split(',')]
	mapping[int(d[0])] = tos

groups = 0

while len(mapping) > 0:
	first_key = [x for x in mapping.keys()][0]
	to_visit = [first_key]
	visited = []
	while to_visit:
		id = to_visit.pop()
		visited.append(id)
		for n in mapping[id]:
			if not n in visited:
				to_visit.append(n)
	groups += 1
	if part2:
		for k in visited:
			if k in mapping:
				del mapping[k]
	else:
		break

r = groups if part2 else len(visited)

repres(r, part2)
