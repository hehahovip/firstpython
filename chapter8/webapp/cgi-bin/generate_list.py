#! /usr/bin/python3

import glob

import kelly6
import yate

data_files = glob.glob("data/*.txt")
athletes = kelly6.loadfiles(data_files)

print(yate.start_response())
print(yate.include_header("Coach Kelly's List of Athletes"))
print(yate.start_form("generate_timing_data.py"))
print(yate.para("Select an athlete from the list to work with:"))
for each_athlete in athletes:
    print(yate.radio_button("which_athlete", each_athlete.name))
print(yate.end_form("Select"))
print(yate.include_footer({"Home": "/index.html"}))
