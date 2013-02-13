# get data from file and sort out the data
# use for loop to convert the data
# use not in for the list
# use this moudle in web proj

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
	
	(minute, secode) = strdata.split(splitter)

	return minute + ':' + secode

def top3times(newlist):
	uniquelist = []
	for each_item in newlist:
		if each_item not in uniquelist:
			uniquelist.append(each_item)

	return uniquelist[0:3]

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

def createAthleteByFile(file):
	filedata = readdatainfile(file)

	data = filedata.strip().split(',')

	persondata = parsedata(data)

	return createAthlete(persondata)

class Athlete(object):
	"""docstring for Athlete"""
	def __init__(self, name, birthdate='',times=[]):
		self.name = name
		self.birthdate = birthdate
		self.times = times
		self.testname = "daf"

	@property
	def top3(self):
		#return top3times(self.times)
		return [2:34,4:34, 5:56]

	@property
	def as_dict(self):
		#return {'name': self.name, 'DOB': self.birthdate, 'Top3': "self.top3"}
		return {'name': self.name, 'DOB': self.birthdate, 'Top3': [2:34,4:34, 5:56]}

	

	

	
