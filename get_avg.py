import sys

a = sys.argv[1]
b = sys.argv[2]

total_sim = 0
count = 0
for line in sys.stdin:
    _, _, s = line.split('|')
    s = int(s)
    total_sim += s
    count += 1
print(a+'|'+b+'|'+str(total_sim/float(count)))
