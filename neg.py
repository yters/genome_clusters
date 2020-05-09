import sys
for line in sys.stdin:
    a, b, c = line.split('|')
    print(a+'|'+b+'|'+str(-float(c)))
