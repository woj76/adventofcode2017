#!/usr/bin/python3

from aoc import repres
import itertools

file = open("../data/day04.txt", "rt")
data = [x.split(' ') for x in file.read().strip().split('\n')]
file.close()

part2 = True
r = 0

for x in data:
	l = len(x)
	ok = True
	for i in range(l):
		for j in range(i+1, l):
			if part2:
				if x[i] in ["".join(y) for y in itertools.permutations(x[j])]:
					ok = False
			elif x[i] == x[j]:
				ok = False 
	if ok:
		r += 1

repres(r, part2)
