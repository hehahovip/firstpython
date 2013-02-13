#! /usr/bin/python3

import cgi

import cgitb
cgitb.enable()

import kelly6
import yate
import glob

data_files = glob.glob("data/*.txt")
athletes = kelly6.loadfiles(data_files)

form_data = cgi.FieldStorage()
athlete_name = form_data['which_athlete'].value

athlete = None

for each_athlete in athletes:
	if each_athlete.name == athlete_name:
		athlete = each_athlete
	else:
		pass

print(yate.start_response())
print(yate.include_header("Coach Kelly's Timing Data"))    
print(yate.header("Athlete: " + athlete_name + ", DOB: " +
                      athlete.birthdate + "."))
print(yate.para("The top times for this athlete are:"))
print(yate.u_list(athlete.top3()))
print(yate.include_footer({"Home": "/index.html",
                           "Select another athlete": "generate_list.py"}))

