#! /usr/bin/python3

# Step 2: write a new CGI script to handle the new data request.
import json
import glob
import yate
import cgi
import athletemodel
from athletemodel import Athlete

		
athletes = []
data_files = glob.glob("data/*.txt")
for each_file in data_files:
	athlete = Athlete()
	athlete.loaddatabyfile(each_file)
	athletes.append(athlete)

form_data = cgi.FieldStorage()
athelete_name = form_data['which_athlete'].value

#athelete_name = 'James Lee'

#print("athelete name:", athelete_name)

athlete = None
for each_athlete in athletes:
	#print(each_athlete.name)
	if athelete_name == each_athlete.name:
		athlete = each_athlete
	else:
		pass

print(yate.start_response('application/json'))
print(json.dumps(athlete.as_dict()))