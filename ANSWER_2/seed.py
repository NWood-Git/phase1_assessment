import sqlite3
import os
import schema

DIRPATH = os.path.dirname(__file__)
DBFILENAME = "college.db"
DBPATH = os.path.join(DIRPATH,DBFILENAME)

dbpath = DBPATH


def seed(dbpath):
    schema.schema(dbpath)#to rerun the schema clear the tables before running this code 

    campuses = [
        ("New York","NY"), # pk 1
        ("Houston","TX")]  # pk 2

    students = [
        ("Walker", "Lockett", 3.1, 1),# pk 1
        ("Casey", "Coleman", 2.7, 1),# pk 2
        ("Franklyn", "Kilome", 3.8, 1),# pk 3
        ("Hecton", "Santiago", 2.9, 1),# pk 4
        ("Framber", "Valdez", 3.9, 2),# pk 5
        ("Brad", "Peacock", 2.8, 2),# pk 6
        ("Reymin", "Guduan", 3.5, 2),# pk 7
        ("Gerrit", "Cole", 3.0, 2)]# pk 8

    with sqlite3.connect(dbpath) as connection:
        cursor = connection.cursor()
        SQL = """INSERT INTO campuses(city, state) VALUES(?,?);"""
        for campus in campuses:
            cursor.execute(SQL,campus)

    with sqlite3.connect(dbpath) as connection:
        cursor = connection.cursor()
        SQL = """INSERT INTO students(first_name, last_name, gpa, campus_pk) VALUES(?,?,?,?);"""
        for student in students:
            cursor.execute(SQL,student)
            



if __name__ == "__main__":
    seed(dbpath) #commented out after run