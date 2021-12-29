#!/usr/bin/python3

from aoc import repres

file = open("../data/day24.txt", "rt")
data = set([tuple([int(y) for y in x.split('/')]) for x in file.read().strip().split('\n') if x != ''])
file.close()

part2 = True

max_strength = float('-inf')
max_length = float('-inf')

def try_build(l, next_port, strength, available):
	global max_strength
	global max_length
	if part2:
		if l > max_length:
			max_length = l
			max_strength = max(strength,max_strength)
	else:
		max_strength = max(strength,max_strength)
	for (i,o) in available:
		if i == next_port:
			try_build(l+1, o, strength + i + o, available - {(i,o)})
		elif o == next_port:
			try_build(l+1, i, strength + i + o, available - {(i,o)})

try_build(0, 0, 0, data)

repres(max_strength, part2)
