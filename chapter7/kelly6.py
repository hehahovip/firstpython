# import kelly5.py
import glob
import kelly5

#data_files = glob.glob("*.txt")

def loadfiles(filelist):
	athletes = []
	for each_file in filelist:
		athlete = kelly5.createAthleteByFile(each_file)
		athletes.append(athlete)
	return athletes
'''for each_file in data_files:
	print("read file: ", each_file)
	athlete = kelly5.createAthleteByFile(each_file)
	print("name: ", athlete.name)
	print("birthdate: ", athlete.birthdate)
	print("top 3 time records: ", athlete.top3())'''
