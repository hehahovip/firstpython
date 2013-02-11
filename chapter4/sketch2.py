# use with open for catch the file not found exception.

with open('sketch1.txt', 'r') as data:
	mandata = list()
	otherdata = list()
	for each_line in data:
		try:
			if not each_line.find(":") == -1:
				(role, sentence) = each_line.split(":")
				print("role : ", role)
				print("spoken : ", sentence)
				if each_line.startswith("Man") == 1:
					mandata.append(each_line)
				elif each_line.startswith("Other Man") == 1:
					otherdata.append(each_line)
				else:
					print("Can't parse this line:", each_line)

		 
		except ValueError as e:
			print("error: ", e)
