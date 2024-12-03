MIN_DIF = 1
MAX_DIF = 3
TOLERANCE = 1

def analyze( l:list, bad:int=0, skip:int=None) -> bool:
    decending = False
    if skip == 0:
        n1 = l[1]
        n2 = l[2]
    elif skip == 1:
        n1 = l[0]
        n2 = l[2]
    else:
        n1 = l[0]
        n2 = l[1]
    if bad > TOLERANCE:
        return 0
    if n1 > n2:
        decending = True
    if skip == 4:
        pass
    for i in range(len(l)-1):
        if skip == 0 == i:
            continue
        elif skip == len(l)-1 and (i == skip or i+1 == skip):
            break
        elif i == skip:
            n1 = l[i-1]
            n2 = l[i+1]
        elif i+1 == skip:
            n1 = l[i]
            n2 = l[i+2]
        else:
            n1 = l[i]
            n2 = l[i+1]
        dif = abs(n1 - n2)
        if dif < MIN_DIF or dif > MAX_DIF:
            for j in range(len(l)):
                if analyze(l, bad+1, j):
                    return 1
            return 0
        elif decending and n2 > n1: # decending
            for j in range(len(l)):
                if analyze(l, bad+1, j):
                    return 1
            return 0
        elif not decending and n1 > n2: # acending
            for j in range(len(l)):
                if analyze(l, bad+1, j):
                    return 1
            return 0
    return 1

good_reports = 0
with open('input1.txt') as infile:
    for line in infile.readlines():
        l = [int(x) for x in line.split(' ')]
        r = analyze(l)
        good_reports += r
print(good_reports)