#!/usr/bin/python3

from aoc import repres

file = open("../data/day07.txt", "rt")
data = [x for x in file.read().strip().split('\n')]
file.close()

part2 = False
r = ""

deps = {}

for d in data:
	kd = d.split(' -> ')
	[key,weight] = kd[0].split(' ')
	if len(kd) == 1:
		l = []
	else:
		l = kd[1].split(', ')	
	deps[key] = (int(weight.replace('(', '').replace(')','')), l)

for key in deps.keys():
	if deps[key][1] == []:
		continue
	found = False
	for w,l in deps.values():
		if key in l:
			found = True
	if not found:
		r = key
		break

repres(r, part2)

part2 = True

weights = {}

def calc_weights(node):
	w, l = deps[node]
	for n in l:
		calc_weights(n)
	weights[node] = w + sum([weights[n] for n in l])

calc_weights(r)

def check_weight(node, correct_weight):
	w, l = deps[node]
	if len(l) == 0:
		return correct_weight
	sw = [weights[sn] for sn in l]
	if all([w == sw[0] for w in sw]):
		return w + correct_weight - weights[node]
	next_node = l[[sw.count(w) for w in sw].index(1)]
	return check_weight(next_node, [w for w in sw if w != weights[next_node]][0])

repres(check_weight(r, weights[r]), part2)

