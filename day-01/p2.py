l1 = []
d1 = {}
d2 = {}
with open('input1.txt', 'r') as input_file:
    for line in input_file.readlines():
        n1, n2 = line.split('   ')
        n1 = int(n1)
        n2 = int(n2)
        l1.append(n1)
        c1 = d1.get(n1, 0)
        d1[n1] = c1 + 1
        c2 = d2.get(n2, 0)
        d2[n2] = c2 + 1
        

similarity =  0
for k1 in l1:
    c2 = d2.get(k1, 0) * k1
    similarity += c2


print(similarity)