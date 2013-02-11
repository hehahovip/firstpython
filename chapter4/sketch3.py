# check type of variable
# parse data from file and write it to new file.
# use with open for catch the file not found exception.

import pickle

with open('sketch.txt', 'r') as data:
	mandata = []
	otherdata = list()

	if type(mandata) is list:
		print("mandata is a list")

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

	print("man data: " + str(mandata))
	print("other data: " + str(otherdata))

with open('man_data.txt', 'wb') as man_data, open('other_data.txt', 'wb') as other_data:
	pickle.dump(mandata, file=man_data)
	pickle.dump(otherdata, file=other_data)
