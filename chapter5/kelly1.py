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


file_james = "james.txt"
file_julie = "julie.txt"
file_mikey = "mikey.txt"
file_sarah = "sarah.txt"

filedata = readdatainfile(file_james)


newlist = [sanitize(each_item) for each_item in filedata.strip().split(',')] 

print("newlist: ", newlist)
print("sorted list: ", sorted(newlist))
sortlist = newlist.sort()
print("sort list: ", sortlist)



uniquelist = []
for each_item in newlist:
	if each_item not in uniquelist:
		uniquelist.append(each_item)


print(uniquelist[0:3])