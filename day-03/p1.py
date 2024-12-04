import re
import sys

mul_pattern = r'mul\(\d+,\d+\)'
extract_num_pattern = r'mul\((\d+),(\d+)\)'

with open(sys.argv[1], 'r') as infile:
	total = 0
	for line in infile.readlines():
		matches = re.findall(mul_pattern, line)
		for mul_str in matches:
			muls = re.findall(extract_num_pattern, mul_str)
			for x, y in muls:
				total += int(x) * int(y)

print(total)