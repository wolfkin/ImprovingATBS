import os
totalSize = 0

workingDirectory = r'C:\\Python38'

for filename in os.listdir(workingDirectory):
	if not os.path.isfile(os.path.join(workingDirectory, filename)):
		continue
	totalSize = totalSize + os.path.getsize(os.path.join(workingDirectory, filename))

print('Total size: ' + str(totalSize))
