import re
import sys

mul_pattern = r"(mul\(\d+,\d+\))|(do\(\))|(don't\(\))"
extract_num_pattern = r'mul\((\d+),(\d+)\)'

with open(sys.argv[1], 'r') as infile:
	total = 0
	do = True
	for line in infile.readlines():
		matches = re.findall(mul_pattern, line)
		for mul_str in matches:
			if 'do' in mul_str[1]:
				do = True
				continue
			elif "don't" in mul_str[2]:
				do = False
				continue
			if not do:
				continue
			mul_str = mul_str[0]
			muls = re.findall(extract_num_pattern, mul_str)
			for x, y in muls:
				total += int(x) * int(y)

print(total)