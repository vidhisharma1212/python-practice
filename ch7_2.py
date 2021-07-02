sil = open('ch6_4.py')
for line in sil:
    line=line.rstrip()
    if line.startswith('print'):
        print(line)

# or
for line in sil:
    line=line.rstrip()
    if not line.startswith('print'):
        continue
    print(line)