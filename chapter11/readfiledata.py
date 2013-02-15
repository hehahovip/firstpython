import time

class LineData(object):
	"""docstring for LineData"""
	def __init__(self, type, data = []):
		self.type = type
		self.data = data
		self.formateddata = []

	def convert2time(self):
		formatedlist = []
		for each_item in self.data:
			formatedtime = []
			for each_time in each_item:
				formatedtime.append(time2secs(format_time(eachtime)))
			formatedlist.append(formatedtime)


def format_time(time_string):
    tlen = len(time_string)
    if tlen < 3:
        original_format = '%S'       
    elif tlen < 6:
        original_format = '%M:%S'
    else:
        original_format = '%H:%M:%S'
    time_string = time.strftime('%H:%M:%S', time.strptime(time_string, original_format))
    return(time_string)

def time2secs(time_string):
    time_string = format_time(time_string)
    (hours, mins, secs) = time_string.split(':')
    seconds = int(secs) + (int(mins)*60) + (int(hours)*60*60)
    return(seconds)

def secs2time(seconds):
    return(time.strftime('%H:%M:%S', time.gmtime(seconds)))


def parse_title_line(titleline):
	titles = titleline.strip().split(',')
	return titles

def parse_data_line(dataline):
	data = dataline.strip().split(',')
	return data

def find_it(rowtype, timestr, dictdata):
	time = time2secs(format_time(timestr))

	rowdict = dictdata[rowtype]

	max = 999999
	tempdiff = 0
	temp = None
	for each_time in sorted(rowdict.keys(), reverse=True):
		each_second = time2secs(format_time(each_time))
		diff = time - each_second
		if diff == 0 :
			return dictdata[rowtype][each_time]
		elif diff > 0:
			if abs(tempdiff) > abs(diff):
				return dictdata[rowtype][each_time] 
			else:
				if temp == None:
					return dictdata[rowtype][each_time]
				else:
					return dictdata[rowtype][temp]
		else:
			# diff > 0
			temp = each_time
			tempdiff = diff
	# nothing found, return the min
	return dictdata[rowtype][temp]


def load_file():
	filepath = 'PaceData.csv'
	dictdata = {}
	with open(filepath) as filedata:
		titleline  = filedata.readline()
		titles = parse_title_line(titleline)
		titles.pop(0)

		datalist = []
		for each_line in filedata:
			linedata = parse_data_line(each_line)
			rowtype = linedata.pop(0)
			objectdata = LineData(rowtype, linedata)
			objectdata.convert2time
			datalist.append(objectdata)

			inner_dict = {}
			for i in range(len(titles)):
				inner_dict[format_time(linedata[i])] = titles[i]

			dictdata[rowtype] = inner_dict

		return dictdata

#dictdata = load_file()
#userrowtype = input("Please input row type:")
#userdata = input("Please input your data:")



#print(find_it(userrowtype, userdata, dictdata))