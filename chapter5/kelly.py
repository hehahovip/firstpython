# get data from file and sort out the data
# use for loop to convert the data




def readdatainfile(filename):
	with open(filename) as filedata:
		return filedata.readline()



file_james = "james.txt"
file_julie = "julie.txt"
file_mikey = "mikey.txt"
file_sarah = "sarah.txt"

filedata = readdatainfile(file_james)
templist = filedata.strip().split(',')
print(templist)
for time in templist:
	print(time)
