import sys

max_sim = 0
max_sim_line = None
for line in sys.stdin:
    a, b, s = line.split('|')
    s = int(s)
    if s > max_sim:
        max_sim = s
        max_sim_line = line.strip()
print(max_sim_line)
