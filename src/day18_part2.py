#!/snap/bin/pypy3

from aoc import repres
from collections import deque

with open("../data/day18.txt", "rt") as file:
	data = file.read().strip().split('\n')

def get_reg(regs, n):
	if n not in regs:
		regs[n] = 0
	return regs[n]

def get_val(regs, s):
	try:
		return int(s)
	except:
		return get_reg(regs, s)

reg_list = [{'p' : 0, 'snd_count' : 0}, {'p' : 1, 'snd_count' : 0}]
qs = [deque(), deque()]
pc = [0, 0]
progress = [True,True]

p_id = 0

while True in progress:
	op_id = (p_id + 1) % 2
	progress[p_id] = False
	i = pc[p_id]
	regs = reg_list[p_id]
	sq = qs[p_id]
	rq = qs[op_id]
	ins = data[i].split(' ')
	if ins[0] == "jgz":
		z = get_val(regs, ins[1])
		if z > 0:
			i += get_val(regs, ins[2])
		else:
			i += 1
	else:
		if ins[0] == "snd":
			sq.append(get_val(regs, ins[1]))
			regs['snd_count'] += 1
			i += 1
			if pc[op_id] < len(data):
				progress[op_id] = True
		elif ins[0] == "set":
			regs[ins[1]] = get_val(regs, ins[2])
			i += 1
		elif ins[0] == "add":
			regs[ins[1]] = get_reg(regs, ins[1]) + get_val(regs, ins[2])
			i += 1
		elif ins[0] == "mul":
			regs[ins[1]] = get_reg(regs, ins[1]) * get_val(regs, ins[2])
			i += 1
		elif ins[0] == "mod":
			regs[ins[1]] = get_reg(regs, ins[1]) % get_val(regs, ins[2])
			i += 1
		elif ins[0] == "rcv":
			if len(rq) > 0:
				regs[ins[1]] = rq.popleft()
				i += 1
	if i != pc[p_id] and i < len(data):
		progress[p_id] = True
		pc[p_id] = i
	if not progress[p_id]:
		p_id = (p_id + 1) % 2

repres(reg_list[1]['snd_count'], True)
