#!/usr/bin/python3

from aoc import repres

file = open("../data/day08.txt", "rt")
data = [x for x in file.read().strip().split('\n')]
file.close()

part2 = True
r = float('-inf')

mem = {}

def lookup(id):
	if not id in mem.keys():
		mem[id] = 0
	return mem[id]

for d in data:
	[reg1, op, op_const, _, reg2, cond_op, cond_const] = d.split(' ')
	op_const = int(op_const)
	cond_const = int(cond_const)
	v1 = lookup(reg1)
	v2 = lookup(reg2)
	if cond_op == "==":
		cond = (v2 == cond_const)
	elif cond_op == "!=":
		cond = (v2 != cond_const)
	elif cond_op == "<":
		cond = (v2 < cond_const)
	elif cond_op == ">":
		cond = (v2 > cond_const)
	elif cond_op == "<=":
		cond = (v2 <= cond_const)
	elif cond_op == ">=":
		cond = (v2 >= cond_const)
	if cond:
		nv = v1 + (op_const if op == "inc" else -op_const)
		mem[reg1] = nv
		if part2:
			r = max(r, nv)

if not part2:
	r = max(mem.values())

repres(r, part2)
