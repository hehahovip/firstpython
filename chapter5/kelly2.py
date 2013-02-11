# get data from file and sort out the data
# use for loop to convert the data
# use not in for the list




def readdatainfile(filename):
	with open(filename) as filedata:
		return filedata.readline()

def sanitize(strdata):
	if '.' in strdata:
		splitter = '.'
	elif '-' in strdata:
		splitter = '-'
	else:
		return strdata
	
	(minute, secode) = strdata.split(splitter)

	return minute + ':' + secode

def readfile(filename):
	filedata = readdatainfile(filename)


	newlist = [sanitize(each_item) for each_item in filedata.strip().split(',')] 

	#print(newlist)
	#print(sorted(newlist))



	uniquelist = []
	for each_item in newlist:
		if each_item not in uniquelist:
			uniquelist.append(each_item)


	print(filename + " data: " , uniquelist[0:3])


file_james = "james.txt"
file_julie = "julie.txt"
file_mikey = "mikey.txt"
file_sarah = "sarah.txt"

readfile(file_james)
readfile(file_julie)
readfile(file_mikey)
readfile(file_sarah)