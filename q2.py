strings = []
s = 'a'
while s != 'stop' and s!= 'Stop':
    s = input()
    strings.append(s)
    

short = 0
long = 0
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
