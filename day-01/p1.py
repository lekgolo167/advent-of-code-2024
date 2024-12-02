l1 =[]
l2 = []
with open('input1.txt', 'r') as input_file:
    for line in input_file.readlines():
        n1, n2 = line.split('   ')
        l1.append(int(n1))
        l2.append(int(n2))

l1.sort()
l2.sort()

total = 0
for n1, n2 in zip(l1, l2):
    total += abs(n1-n2)

print(total)