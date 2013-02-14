import sqlite3
import glob
from athletemodel import Athlete

connection = sqlite3.connect('coachdata.sqlite')
cursor = connection.cursor()


athletes = []
data_files = glob.glob("../data/*.txt")
for each_file in data_files:
	athlete = Athlete()
	athlete.loaddatabyfile(each_file)
	athletes.append(athlete)

for each_ath in athletes:
    name = each_ath.name
    dob = each_ath.birthdate
    cursor.execute("INSERT INTO athletes (name, dob) VALUES (?, ?)", (name, dob))
    connection.commit()

connection.close()