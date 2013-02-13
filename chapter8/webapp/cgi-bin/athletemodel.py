class Athlete(object):
	"""docstring for Athlete"""
	def __init__(self, name=None, birthdate='',times=[]):
		self.name = name
		self.birthdate = birthdate
		self.times = times

	def sanitized(self, strdata):
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

	def parsedata(self, data):
		self.name = data.pop(0)
		self.birthdate = data.pop(0)
		newlist = [self.sanitized(item) for item in data]
		self.times = newlist
		return

	def loaddatabyfile(self, filename):
		with open(filename) as filedata:

			data = filedata.readline().strip().split(',')
			self.parsedata(data)

	def top3times(self, list):
		uniquelist = []
		for each_item in list:
			if each_item not in uniquelist:
				uniquelist.append(each_item)

		return uniquelist[0:3]

	@property
	def top3(self):
		return self.top3times(self.times)

	def as_dict(self):
		return {'name': self.name, 'DOB': self.birthdate, 'Top3': self.top3}
