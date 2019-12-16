import sqlite3
import os
import schema

DIRPATH = os.path.dirname(__file__)
DBFILENAME = "college.db"
DBPATH = os.path.join(DIRPATH,DBFILENAME)

dbpath = DBPATH

#Q: After inserting the rows, update Franklyn Kilome's GPA to 2.5
def update_gpa(gpa, student_pk):
    with sqlite3.connect(dbpath) as connection:
        cursor = connection.cursor()
        cursor.execute("UPDATE students SET gpa=? WHERE pk=?",(gpa, student_pk))

#Q: Write a python function that takes a city and state argument 
# and returns the average GPA for the students on that campus.

def avg_campus_gpa(city, state):
    with sqlite3.connect(dbpath) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        SQL = "SELECT gpa FROM students JOIN campuses ON students.campus_pk = campuses.pk WHERE campuses.city=? AND campuses.state=?;"
        cursor.execute(SQL, (city, state))
        rows = cursor.fetchall()
        gpas = []
        for row in rows:
            row = dict(row)
            gpas.append(row['gpa'])
        sum_gpa = sum(gpas)
        count_gpa = len(gpas)
        return round((sum_gpa / count_gpa),2)

# Write a SQL SELECT statement to get the last names of all students in New York with a GPA over 3.0. 
# Do not select based on an integer foreign key, use a join and select by the city name.
SQL = "SELECT * FROM students JOIN campuses ON students.campus_pk = campuses.pk WHERE campuses.city = "New York" AND students.gpa > 3.0;"


if __name__ == "__main__":
    # update_gpa(2.5,3) #Ran then commented out
    print(avg_campus_gpa("New York","NY"))