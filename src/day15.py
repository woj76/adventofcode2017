#!/snap/bin/pypy3

from aoc import repres

part2 = True

gen_a_n = 16807
gen_b_n = 48271
m = 2147483647

# User specific input
gen_a = 722
gen_b = 354

score = 0

for _ in range(5000000 if part2 else 40000000):
	gen_a = gen_a * gen_a_n % m
	gen_b = gen_b * gen_b_n % m
	if part2:
		while gen_a % 4 != 0:
			gen_a = gen_a * gen_a_n % m
		while gen_b % 8 != 0:
			gen_b = gen_b * gen_b_n % m
	if (gen_a & 0xFFFF) == (gen_b & 0xFFFF):
		score += 1

repres(score, part2)
