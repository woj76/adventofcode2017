#!/snap/bin/pypy3

from aoc import repres

with open("../data/day18.txt", "rt") as file:
	data = file.read().strip().split('\n')

registers = {}

def get_reg(n):
	if n not in registers:
		registers[n] = 0
	return registers[n]

def get_val(s):
	try:
		return int(s)
	except:
		return get_reg(s)


i = 0
last_snd = None

while True:
	ins = data[i].split(' ')
	if ins[0] == "jgz":
		z = get_val(ins[1])
		if z > 0:
			i += get_val(ins[2])
		else:
			i += 1
	else:
		if ins[0] == "snd":
			v = get_val(ins[1])
			last_snd = v
		elif ins[0] == "set":
			registers[ins[1]] = get_val(ins[2])
		elif ins[0] == "add":
			registers[ins[1]] = get_reg(ins[1]) + get_val(ins[2])
		elif ins[0] == "mul":
			registers[ins[1]] = get_reg(ins[1]) * get_val(ins[2])
		elif ins[0] == "mod":
			registers[ins[1]] = get_reg(ins[1]) % get_val(ins[2])
		elif ins[0] == "rcv":
			z = get_val(ins[1])
			if z != 0:
				r = last_snd
				break
		i += 1
	if i >= len(data):
		break

repres(r, False)
