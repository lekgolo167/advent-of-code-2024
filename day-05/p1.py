import sys

page_ordering = {}
possible_updates = []

with open(sys.argv[1], 'r') as infile:
	for line in infile.readlines():
		if '|' in line:
			s = line.split('|')
			before, after = int(s[0]), int(s[1])
			page_order = page_ordering.get(before, [])
			page_order.append(after)
			page_ordering[before] = page_order
		elif ',' in line:
			possible_updates.append([int(x) for x in line.split(',')])

# print(page_ordering)
# print(possible_updates)

def check_order(preceding_pages:list, order:list) -> bool:
	for page in preceding_pages:
		if page in order:
			return False
	return True


def check_possible_orderings(page_ordering:dict, possible_updates:list) -> int:
	total = 0
	for update in possible_updates:
		correct = True
		for i, page in enumerate(update):
			order = page_ordering.get(page)
			preceding_pages = update[:i]
			if order and not check_order(preceding_pages, order):
				correct = False
				break
		if correct:
			total += update[len(update)//2]
	
	return total

answer = check_possible_orderings(page_ordering, possible_updates)
print(f'Answer: {answer}')