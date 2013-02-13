#! /usr/bin/python3

# Step 2: write a new CGI script to handle the new data request.
import json
import glob
import yate
import athletemodel #import Athlete

athletemodel.sayhello()

athletes = []
data_files = glob.glob("data/*.txt")
for each_file in data_files:
	athlete = Athlete()
	athlete.loaddatabyfile(each_file)
	athletes.append(athlete)

names = []
for each_athlete in athletes:
	names.append(each_athlete.name)

print(yate.start_response('application/json'))
print(json.dumps(sorted(names)))

