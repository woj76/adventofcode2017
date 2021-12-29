#!/snap/bin/pypy3

from aoc import repres

state = 'A'
check = 12919244

prog = {}

prog['A'] = [1, +1, 'B', 0, -1, 'C']
prog['B'] = [1, -1, 'A', 1, 1, 'D']
prog['C'] = [1, 1, 'A', 0, -1, 'E']
prog['D'] = [1, 1, 'A', 0, 1, 'B']
prog['E'] = [1, -1, 'F', 1, -1, 'C']
prog['F'] = [1, 1, 'D', 1, 1, 'A']

tape = {0:0}
pos = 0

for _ in range(0, check):
	v = tape[pos] if pos in tape else 0
	i = 0 if v == 0 else 3
	tape[pos] = prog[state][i]
	pos += prog[state][i+1]
	state = prog[state][i+2]

repres(sum(tape.values()), False)
