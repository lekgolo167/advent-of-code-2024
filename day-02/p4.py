MIN_DIF = 1
MAX_DIF = 3
TOLERANCE = 1

def dampener(l:list, bad:int):
    for j in range(len(l)):
        ll = l.copy()
        del ll[j]
        if analyze(ll, bad+1):
            return 1
    return 0

def analyze( l:list, bad:int=0, skip:int=None) -> bool:
    decending = False
    n1 = l[0]
    n2 = l[1]
    if bad > TOLERANCE:
        return 0
    if skip == 4:
        pass
    if n1 > n2:
        decending = True
    for i in range(len(l)-1):
        n1 = l[i]
        n2 = l[i+1]
        dif = abs(n1 - n2)
        if dif < MIN_DIF or dif > MAX_DIF:
            return dampener(l, bad)
        elif decending and n2 > n1: # decending
            return dampener(l, bad)
        elif not decending and n1 > n2: # acending
            return dampener(l, bad)
    return 1

good_reports = 0
with open('input2.txt') as infile:
    for line in infile.readlines():
        l = [int(x) for x in line.split(' ')]
        r = analyze(l)
        good_reports += r
print(good_reports)