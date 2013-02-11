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

def top3times(newlist):
	uniquelist = []
	for each_item in newlist:
		if each_item not in uniquelist:
			uniquelist.append(each_item)

	return uniquelist

def parsedata(data):
	persondata = {}
	persondata['name'] = data.pop(0)
	persondata['birthdate'] = data.pop(0)
	newlist = [sanitize(item) for item in data]
	persondata['times'] = newlist
	return persondata

def createAthlete(persondata):
	a = Athlete(persondata['name'], persondata['birthdate'], persondata['times'])
	return a


class Athlete(object):
	"""docstring for Athlete"""
	def __init__(self, name, birthdate='',times=[]):
		super(Athlete, self).__init__()
		self.name = name
		self.birthdate = birthdate
		self.times = times

	def top3(self):
		return top3times(self.times)


file_james = "james2.txt"
file_julie = "julie2.txt"
file_mikey = "mikey2.txt"
file_sarah = "sarah2.txt"

filedata = readdatainfile(file_james)

data = filedata.strip().split(',')

persondata = parsedata(data)

person = createAthlete(persondata)

print("name: " + person.name + ", birthdate: " + person.birthdate)
print("poped data: ", person.times)
print("top 3 times", person.top3())
