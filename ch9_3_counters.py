counts= dict()
names= ['csev', 'cwen', 'zqian', 'cwen']
for name in names:
    if name in counts:
        x= counts[name]
    else:
        x=0


x= counts.get(name, 0)
print(x)