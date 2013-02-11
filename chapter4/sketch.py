try:
	data = open('sketch.txt')
	mandata = list()
	otherdata = list()
	for each_line in data:
		try:
			if not each_line.find(":") == -1:
				(role, sentence) = each_line.split(":")
				#print("role : ", role)
				#print("spoken : ", sentence)
		 
		except ValueError as e:
			print(e)
except IOError:
	print("File error")
finally:
	data.close()


	
