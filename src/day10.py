#!/snap/bin/pypy3

from aoc import repres

part2 = True

file = open("../data/day10.txt", "rt")
if part2:
	lengths = [ord(x) for x in file.read().strip()]
	lengths.extend([17,31,73,47,23])
else:
	lengths = [int(x) for x in file.read().strip().split(',')]
file.close()

r = 0

hash = [x for x in range(256)]

current_position = 0
current_skip = 0

for _ in range(64 if part2 else 1):
	for l in lengths:
		for rr in range(0, l // 2):
			first_pos = (current_position + rr) % 256
			last_pos = (current_position + l - rr - 1) % 256
			hash[first_pos], hash[last_pos] = hash[last_pos], hash[first_pos]
		current_position += l + current_skip
		current_skip += 1

if part2:
	dense = [0] * 16
	for i in range(16):
		for j in range(16):
			dense[i] ^= hash[i*16 + j]
	r = ""
	for d in dense:
		r += "{:02x}".format(d)
else:
	r = hash[0] * hash[1]

repres(r, part2)
