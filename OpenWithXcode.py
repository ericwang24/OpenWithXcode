def endWith(s, *endstring):
	array = map(s.endswith,endstring)
	if True in array:
		return True
	else:
		return False

import os
import sys

cwd = ''
for i in range(1, len(sys.argv)):
    cwd = cwd + sys.argv[i]

print(str(cwd))
files = os.listdir(cwd)
xcodeFile = ''
for name in files:
	if endWith(name, '.xcworkspace'):
		xcodeFile = name;
		break

if xcodeFile.strip() == '':
	for name in files:
		if endWith(name, '.xcodeproj'):
			xcodeFile = name;
			break

print (str(xcodeFile))
os.system('open ' + cwd + '/' + xcodeFile)
