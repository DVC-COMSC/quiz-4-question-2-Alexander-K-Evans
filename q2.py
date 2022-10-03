strings = []
s = input()
while s != 'stop' and s!= 'Stop':
    strings.append(s)
    s = input()
    
strings.append(s)
short = 0
long = 0
if(len(strings) > 0):
    for i in range(len(strings)):
        if len(strings[i]) > len(strings[long]):
            long = i
        if len(strings[i]) < len(strings[short]):
            short = i
    print(strings[long], strings[short])
# ******************************
# Make your Code
# ******************************


# Requirement
# No need to use list
# All input values are taken one by one separatively.
###
