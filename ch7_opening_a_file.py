s = open('ch6_2.py')
no_of_lines= 0
for cheese in s:
    print(cheese)
    no_of_lines= no_of_lines+1
print("no. of lines are " , no_of_lines)

k= s.read()
print(len(k)) # why is it giving 0