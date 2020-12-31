#!/snap/bin/pypy3

from aoc import repres

with open("../data/day13.txt", "rt") as file:
	data = [tuple(x.split(": ")) for x in file.read().strip().split('\n')]

firewall = {}

for dp,rng in data:
	firewall[int(dp)] = int(rng)

dp = int(dp) + 1

states = [(0,1) for _ in range(dp)]

def next_state():
	for i, (p,s) in enumerate(states):
		if i not in firewall:
			continue
		p += s
		if s > 0 and p == firewall[i] - 1:
			s = -1
		elif s < 0 and p == 0:
			s = 1
		states[i] = (p, s)

r = 0

for i in range(dp):
	if i in firewall:
		if states[i][0] == 0:
			r += i*firewall[i]
	next_state()

repres(r, False)

r = 1

while True:
	all_ok = True
	for dp,rng in firewall.items():
		if (r+dp) % (2*rng-2) == 0:
			all_ok = False
			break
	if all_ok:
		break
	r += 1

repres(r, True)
