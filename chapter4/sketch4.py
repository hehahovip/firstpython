# read dumped data from file.

import pickle

with open('man_data.txt', 'rb') as man_data, open('other_data.txt', 'rb') as other_data:
	mandata = []
	otherdata = list()

	#mandata = man_data.readline()

	mandata = pickle.load(man_data)

	print(mandata)

	for each_item in mandata:
		print(each_item)