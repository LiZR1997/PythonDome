
zidian = {}
with open('D:\\speech.txt') as f:
    lines = f.readline ()
a1 = re.split('\\W+',a)
for zi in a1[:-1]:
for zi in a1[:-1]:
	if(zidian.has_key(zi)):
		zidian[zi] = zidian[zi] + 1
	else:
		zidian[zi] = 1
