letter = 'From somebody@1.3.4. sent to anyone'
h= letter.find('@')
print(h)
j= letter.find(' ', h)
print(j)
d= letter[(h+1):j]
print(d)