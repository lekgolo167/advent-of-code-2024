MIN_DIF = 1
MAX_DIF = 3


def analyze( s:str) -> bool:
    l = [int(x) for x in s.split(' ')]
    decending = False
    n1 = l[0]
    n2 = l[1]
    if n1 > n2:
        decending = True
    for i in range(len(l)-1):
        n1 = l[i]
        n2 = l[i+1]
        dif = abs(n1 - n2)
        if dif < MIN_DIF or dif > MAX_DIF:
            return 0
        elif decending and n2 > n1:
            return 0
        elif not decending and n1 > n2:
            return 0
    return 1

good_reports = 0
with open('input1.txt') as infile:
    for line in infile.readlines():
        r = analyze(line.strip())
        print(r)
        good_reports += r
print(good_reports)