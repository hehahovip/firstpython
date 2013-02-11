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
	elif '.' in strdata:
		splitter = '.'
	else:
		return strdata
	
	print("strdata: ", strdata)

	(minute, secode) = strdata.split(splitter)

	return minute + ':' + secode


file_james = "james2.txt"
file_julie = "julie2.txt"
file_mikey = "mikey2.txt"
file_sarah = "sarah2.txt"

filedata = readdatainfile(file_james)

data = filedata.strip().split(',')

print("data: ", data)
name = data.pop(0)
birthdate = data.pop(0)
print("name: " + name + ", birthdate: " + birthdate)
print("poped data: ", data)
newlist = [sanitize(item) for item in data]

print("newlist", newlist)

print(newlist)
print(sorted(newlist))

uniquelist = []
for each_item in newlist:
	if each_item not in uniquelist:
		uniquelist.append(each_item)


print(uniquelist[0:3])