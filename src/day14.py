#!/snap/bin/pypy3

from aoc import repres

input = 'wenycdww'

part2 = True

def knot_hash(s):
	lengths = [ord(x) for x in s]
	lengths.extend([17,31,73,47,23])
	hash = [x for x in range(256)]
	current_position = 0
	current_skip = 0
	for _ in range(64):
		for l in lengths:
			for rr in range(0, l // 2):
				first_pos = (current_position + rr) % 256
				last_pos = (current_position + l - rr - 1) % 256
				hash[first_pos], hash[last_pos] = hash[last_pos], hash[first_pos]
			current_position += l + current_skip
			current_skip += 1
	dense = [0] * 16
	for i in range(16):
		for j in range(16):
			dense[i] ^= hash[i*16 + j]
	r = ""
	for d in dense:
		r += "{:02x}".format(d)
	return r

r = 0
grid = []

for index in range(128):
	n = format(int(knot_hash(input+"-"+str(index)), 16), 'b').zfill(128)
	if part2:
		grid.append(list(n))
	else:
		r += n.count('1')

def neighbours(y,x):
	ret = []
	if x < 127:
		ret.append((y, x+1))
	if x > 0:
		ret.append((y, x-1))
	if y < 127:
		ret.append((y+1, x))
	if y > 0:
		ret.append((y-1, x))
	return ret

def find_group(y, x):
	visited = [(y,x)]
	visited_index = 0
	while visited_index < len(visited):
		py,px = visited[visited_index]
		visited_index += 1
		for (ny,nx) in neighbours(py,px):
			if grid[ny][nx] == '1' and not (ny,nx) in visited:
				visited.append((ny,nx))
	for (py,px) in visited:
		grid[py][px] = '0'

if part2:
	for y in range(128):
		for x in range(128):
			if grid[y][x] == '1':
				find_group(y, x)
				r += 1

repres(r, part2)
