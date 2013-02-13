def sayhello():
	print("hello world!")

class Athlete(object):
	"""docstring for Athlete"""
	def __init__(self, name=None, birthdate='',times=[]):
		self.name = name
		self.birthdate = birthdate
		self.times = times

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

	def parsedata(data):
		self.name = data.pop(0)
		self.birthdate = data.pop(0)
		newlist = [sanitize(item) for item in data]
		self.times = newlist
		return

	def loaddatabyfile(file):
		with open(filename) as filedata:
			data = filedata.strip().split(',')
			self.parsedata(data)

	def top3times(self, list):
		uniquelist = []
		for each_item in list:
			if each_item not in uniquelist:
				uniquelist.append(each_item)

		return uniquelist[0:3]

	def top3(self):
		return top3times(self.times)

	def as_dict(self):
		return {'name': self.name, 'DOB': self.birthdate, 'Top3': "self.top3"}
