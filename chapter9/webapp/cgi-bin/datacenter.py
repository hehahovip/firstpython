#! /usr/bin/python3

import sqlite3

from athletemodel import Athlete

def get_athletes():
	athletes = []
	connection = sqlite3.connect('coachdata.sqlite')
	cursor = connection.cursor()
	cursor.execute("SELECT name, dob, id from athletes WHERE name=? AND dob=?", (name, dob))
	item = cursor.fetchone()
	athlete = Athlete(item[0], item[0])
    athletes.append(athlete)

    cursor.execute("SELECT value from timing_data WHERE athlete_id=? ", (item[2]))
    ath_times = cursor.fetchall()
    athlete.times.extend(ath_times)

    connection.close()

def add_time_record(name, time):
	connection = sqlite3.connect('coachdata.sqlite')
	cursor = connection.cursor()
	cursor.execute("SELECT  id from athletes WHERE name=?", (name))
	ath_id = cursor.fetchone()[0]

	cursor.execute("insert into timing_data (athlete_id, value) values(?, ?)", (ath_id, time))

	connection.close()

